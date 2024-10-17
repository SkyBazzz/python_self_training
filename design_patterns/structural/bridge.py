"""
This pattern decouples an abstraction from its implementation so that the two can vary independently.
"""


class Implementor:
    def operation_impl(self):
        pass


class Abstraction:
    def __init__(self, implementor):
        self.implementor = implementor

    def operation(self):
        self.implementor.operation_impl()


class ConcreteImplementorA(Implementor):
    def operation_impl(self):
        print("ConcreteImplementorA: Operation implementation")


class ConcreteImplementorB(Implementor):
    def operation_impl(self):
        print("ConcreteImplementorB: Operation implementation")


if __name__ == "__main__":
    implementor_a = ConcreteImplementorA()
    implementor_b = ConcreteImplementorB()

    abstraction_a = Abstraction(implementor_a)
    abstraction_a.operation()

    abstraction_b = Abstraction(implementor_b)
    abstraction_b.operation()
