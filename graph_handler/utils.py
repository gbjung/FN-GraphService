from py2neo import Node

def create_or_update_node(graph, node_data):
    labels = node_data.pop('node_labels')
    node_id = node_data['id']
    found_node = node_exists(graph, node_id)

    if found_node:
        query = f"match (node {{id: {node_id}}})"
        node = found_node[0]['node']
        found_labels = set(node.labels())
        labels_to_remove = [label for label in found_labels if label not in labels]
        labels_to_add = [label for label in labels if label not in found_labels]

        if labels_to_remove or labels_to_add:
            for label in labels_to_remove:
                query += f" remove node:`{label}`"
            for label in labels_to_add:
                query += f" set node:`{label}`"
    else:
        query = f"create (node {{id: {node_id}}})"
        for label in labels:
            query += f" set node:`{label}`"

    properties = []
    for prop, value in node_data.items():
        if isinstance(value, str):
            value = f"'{value}'"
        properties.append(f'{prop}:{value}')

    properties = ", ".join(properties)
    query += f" set node = {{{properties}}}"
    graph.run(query)

def create_or_update_edge(graph, edge_data):
    source = edge_data['source']
    target = edge_data['target']
    label = edge_data['label']
    meta = edge_data.get('meta')

    query = f"match (a {{id: {source}}}), (b {{id: {target}}}) "
    query += f"create (a)-[r:`{label}`]->(b)"
    properties = ['{}:{}'.format('id', edge_data['id'])]

    if meta:
        for prop, value in meta.items():
            if isinstance(value, str):
                value = f"'{value}'"
            properties.append(f'{prop}:{value}')

    properties = ", ".join(properties)
    query += f" set r = {{{properties}}}"
    graph.run(query)

def node_exists(graph, node_id):
    return graph.run(f"match (node {{id: {node_id}}}) return node").data()
