from py2neo.ogm import GraphObject, Property

class Person(GraphObject):
    __primarykey__ = 'fn_id'

    fn_id = Property()

    name_first = Property()
    name_last = Property()
    name_full = Property()

    source_id = Property()
    source = Property()

class Organization(GraphObject):
    __primarykey__ = 'fn_id'

    fn_id = Property()

    name = Property()
    organization_type = Property()

    source_id = Property()
    source = Property()
