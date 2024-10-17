"""
Lets you separate algorithms from the objects on which they operate. It lets you define a new operation
without changing the classes of the elements on which it operates.
"""


class Visitor:
    def visit(self, elemente):
        pass


class Element:
    def accept(self, visitore):
        pass


class ConcreteElementA(Element):
    def accept(self, visitore):
        visitore.visit(self)


class ConcreteElementB(Element):
    def accept(self, visitore):
        visitore.visit(self)


class ConcreteVisitorA(Visitor):
    def visit(self, elemente):
        print("ConcreteVisitorA visits", type(elemente).__name__)


class ConcreteVisitorB(Visitor):
    def visit(self, elemente):
        print("ConcreteVisitorB visits", type(elemente).__name__)


if __name__ == "__main__":
    elements = [ConcreteElementA(), ConcreteElementB()]
    visitors = [ConcreteVisitorA(), ConcreteVisitorB()]

    for element in elements:
        for visitor in visitors:
            element.accept(visitor)
