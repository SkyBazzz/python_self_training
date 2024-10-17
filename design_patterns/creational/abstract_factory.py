"""
The Abstract Factory Pattern provides an interface for creating families of related
or dependent objects without specifying their concrete classes.
"""


class AbstractFactory:
    def create_product_a(self):
        pass

    def create_product_b(self):
        pass


class ConcreteFactory1(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA1()

    def create_product_b(self):
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA2()

    def create_product_b(self):
        return ConcreteProductB2()


class AbstractProductA:
    def operation_a(self):
        pass


class AbstractProductB:
    def operation_b(self):
        pass


class ConcreteProductA1(AbstractProductA):
    def operation_a(self):
        return "ConcreteProductA1: OperationA"


class ConcreteProductA2(AbstractProductA):
    def operation_a(self):
        return "ConcreteProductA2: OperationA"


class ConcreteProductB1(AbstractProductB):
    def operation_b(self):
        return "ConcreteProductB1: OperationB"


class ConcreteProductB2(AbstractProductB):
    def operation_b(self):
        return "ConcreteProductB2: OperationB"


if __name__ == "__main__":
    factory_1 = ConcreteFactory1()
    product_a1 = factory_1.create_product_a()
    product_b1 = factory_1.create_product_b()
    result_a1 = product_a1.operation_a()
    result_b1 = product_b1.operation_b()
    print(result_a1)
    print(result_b1)

    factory_2 = ConcreteFactory2()
    product_a2 = factory_2.create_product_a()
    product_b2 = factory_2.create_product_b()
    result_a2 = product_a2.operation_a()
    result_b2 = product_b2.operation_b()
    print(result_a2)
    print(result_b2)
