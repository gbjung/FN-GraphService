from py2neo import Graph, authenticate
from flask import Blueprint, request, jsonify

import settings
from graph_handler.dummy_data import people, organizations, relationships


authenticate(settings.NEO4J_HOST, settings.NEO4J_USER, settings.NEO4J_PASSWORD)
graph = Graph("https://{}".format(settings.NEO4J_HOST),
              bolt=False)

graph_routes = Blueprint('graph_routes', __name__)

@graph_routes.route('/dummy_graph', methods = ['GET'])
def get_dummy_graph():
    nodes = people + organizations
    return_graph = {"nodes": nodes, "edges": relationships}
    return jsonify(return_graph)

@graph_routes.route('/add_nodes', methods = ['POST'])
def add_nodes():
    new_nodes = request.get_json()
    print(len(new_nodes))
    return jsonify("success")
