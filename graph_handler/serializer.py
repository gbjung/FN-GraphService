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
