"""
The Factory Method Pattern provides an interface for creating objects in a superclass,
but allows subclasses to alter the type of objects that will be created.
"""


class Creator:
    def factory_method(self) -> "Product":
        pass

    def operation(self):
        return f"Creator: {self.factory_method().operation()}"


class Product:
    def operation(self):
        pass


class ConcreteCreatorA(Creator):
    def factory_method(self):
        return ConcreteProductA()


class ConcreteCreatorB(Creator):
    def factory_method(self):
        return ConcreteProductB()


class ConcreteProductA(Product):
    def operation(self):
        return "ConcreteProductA: Operation"


class ConcreteProductB(Product):
    def operation(self):
        return "ConcreteProductB: Operation"


if __name__ == "__main__":
    creator_a = ConcreteCreatorA()
    result_a = creator_a.operation()
    print(result_a)  # Creator: ConcreteProductA: Operation

    creator_b = ConcreteCreatorB()
    result_b = creator_b.operation()
    print(result_b)  # Creator: ConcreteProductB: Operation
