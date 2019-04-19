def PersonSerializer(person):
    person_json = {
        'id': person.fn_id,
        'first_name': person.name_first,
        'last_name': person.name_last,
        'name_full': person.name_full,
        'node_type': 'person',
        'source': person.source,
        'source_id': person.source_id
    }

    return person_json

def ResultSerializer(results):
    '''
    Serializes an node - relationship - node return
    into a list of unique nodes and edges
    '''
    node_ids = set()
    nodes = []
    edges = []
    for result in results:
        source = dict(result['a'])
        target = dict(result['b'])
        label = result['type(r)']
        relationship_meta = dict(result['r'])
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

    return nodes, edges
