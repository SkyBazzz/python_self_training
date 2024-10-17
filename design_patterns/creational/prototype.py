"""
The Prototype Pattern creates new objects by cloning existing objects,
thus avoiding the overhead of creating new objects from scratch.
"""

import copy


class Prototype:
    def clone(self):
        pass


class ConcretePrototype1(Prototype):
    def __init__(self):
        self.attribute_a = "Attribute A"
        self.attribute_b = "Attribute B"

    def clone(self):
        return copy.deepcopy(self)


class ConcretePrototype2(Prototype):
    def __init__(self):
        self.attribute_c = "Attribute C"
        self.attribute_d = "Attribute D"

    def clone(self):
        return copy.deepcopy(self)


if __name__ == "__main__":
    prototype1 = ConcretePrototype1()
    clone1 = prototype1.clone()
    print(prototype1.attribute_a)
    prototype1.attribute_a = "You've been changed"
    print(clone1.attribute_a)

    prototype2 = ConcretePrototype2()
    clone2 = prototype2.clone()
    print(clone2.attribute_c)
