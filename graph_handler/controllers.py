from py2neo import Graph, authenticate, NodeSelector
from flask import Blueprint, request, jsonify

import settings
from graph_handler.dummy_data import people, organizations, relationships
from graph_handler.utils import create_or_update_node, create_or_update_edge

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
    node_ids = set()
    nodes = []
    edges = []
    query = "match (a)-[r]-(b) return a, type(r), r, b"
    results = graph.run(query).data()
    for result in results:
        print(result)
        source = dict(result['a'])
        target = dict(result['b'])
        label = result['type(r)']
        relationship_meta = dict(result['r'])
        print(relationship_meta)
        relationship_id = relationship_meta.pop('id')

        if source['id'] not in node_ids:
            nodes.append(source)
            node_ids.add(source['id'])

        if target['id'] not in node_ids:
            nodes.append(target)
            node_ids.add(target['id'])

        edge = {
          "id": relationship_id,
          "source": source['id'],
          "target": target['id'],
          "label": label,
          "meta": relationship_meta
        }

        edges.append(edge)

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
    edges = request.get_json()
    for edge_data in edges:
        create_or_update_edge(graph, edge_data)

    return jsonify("success")
