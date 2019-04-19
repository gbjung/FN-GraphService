from py2neo.ogm import GraphObject, Property

class Labels():
    def __init__(self, names=[]):
        self.names = names

    def __get__(self, instance, owner):
        return [instance.__ogm__.node.has_label(name) for name in self.names]

    def __set__(self, instance, values):
        if values:
            for value in values:
                instance.__ogm__.node.add_label(value)
        else:
            for value in values:
                instance.__ogm__.node.remove_label(value)

class Property(object):
    """ A property definition for a :class:`.GraphObject`.
    """

    def __init__(self, key=None):
        self.key = key
        print(key)
        
    def __get__(self, instance, owner):
        return instance.__ogm__.node[self.key]

    def __set__(self, instance, value):
        instance.__ogm__.node[self.key] = value

class Person(GraphObject):
    __primarykey__ = 'fn_id'
    __primarylabel__ = "Person"

    fn_id = Property()

    name_first = Property()
    name_last = Property()
    name_full = Property()
    labels = Labels()
    source_id = Property()
    source = Property()

class Organization(GraphObject):
    __primarykey__ = 'fn_id'

    fn_id = Property()

    name = Property()
    organization_type = Property()

    source_id = Property()
    source = Property()
