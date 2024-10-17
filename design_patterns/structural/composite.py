"""
This pattern allows you to compose objects into tree structures to represent part-whole hierarchies.
 Composite lets clients treat individual objects and compositions of objects uniformly.
"""


class Component:
    def __init__(self, name):
        self.name = name

    def operation(self):
        pass


class Leaf(Component):
    def operation(self):
        print(f"Leaf {self.name}: Operation")


class Composite(Component):
    def __init__(self, name):
        super().__init__(name)
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def operation(self):
        print(f"Composite {self.name}: Operation")
        for child in self.children:
            child.operation()


if __name__ == "__main__":
    leaf1 = Leaf("1")
    leaf2 = Leaf("2")
    leaf3 = Leaf("3")
    composite1 = Composite("A")
    composite1.add(leaf1)
    composite1.add(leaf2)
    composite2 = Composite("B")
    composite2.add(leaf3)
    composite1.add(composite2)
    composite1.operation()
