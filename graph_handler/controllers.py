from py2neo import Graph, authenticate, NodeSelector
from flask import Blueprint, request, jsonify

import settings
from graph_handler.dummy_data import people, organizations, relationships
from graph_handler.utils import create_or_update_node, create_or_update_edge
from graph_handler.serializer import ResultSerializer

authenticate(settings.NEO4J_HOST, settings.NEO4J_USER, settings.NEO4J_PASSWORD)
graph = Graph("https://{}".format(settings.NEO4J_HOST),
              bolt=False)

graph_routes = Blueprint('graph_routes', __name__)

@graph_routes.route('/dummy_graph', methods=['GET'])
def get_dummy_graph():
    nodes = people + organizations
    return_graph = {"nodes": nodes, "edges": relationships}
    return jsonify(return_graph)

@graph_routes.route('/real_graph', methods=['GET'])
def real_graph():
    query = "match (a)-[r]-(b) return a, type(r), r, b"
    results = graph.run(query).data()
    nodes, edges = ResultSerializer(results)
    return_graph = {"nodes": nodes, "edges": edges}

    return jsonify(return_graph)

@graph_routes.route('/nodes', methods=['POST'])
def create_or_update_nodes():
    nodes = request.get_json()
    for node_data in nodes:
        create_or_update_node(graph, node_data)

    return jsonify("success")

@graph_routes.route('/edges', methods=['POST'])
def create_or_update_edges():
    '''
    Currently only supports creating edges :'(
    '''
    edges = request.get_json()
    for edge_data in edges:
        create_or_update_edge(graph, edge_data)

    return jsonify("success")

@graph_routes.route('/expand_node/<node_id>', methods=['GET'])
def expand_node(node_id):
    '''
    Currently only supports creating edges :'(
    '''
    query = f"match (a {{id:{node_id}}})-[r]-(b) return a, type(r), r, b"
    results = graph.run(query).data()
    nodes, edges = ResultSerializer(results)
    return_graph = {"nodes": nodes, "edges": edges}
    return jsonify(return_graph)
