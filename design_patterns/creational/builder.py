"""
The Builder Pattern separates the construction of a complex object from its representation,
allowing the same construction process to create different representations.
"""


class Product:
    def __init__(self):
        self.parts = []

    def add_part(self, part):
        self.parts.append(part)

    def list_parts(self):
        result = f"Product parts: {', '.join(self.parts)}"
        return result


class Builder:
    def build_part_a(self):
        pass

    def build_part_b(self):
        pass

    def build_part_c(self):
        pass

    def get_product(self):
        pass


class ConcreteBuilder1(Builder):
    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        self.product.add_part("PartA1")

    def build_part_b(self):
        self.product.add_part("PartB1")

    def build_part_c(self):
        self.product.add_part("PartC1")

    def get_product(self):
        return self.product


class ConcreteBuilder2(Builder):
    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        self.product.add_part("PartA2")

    def build_part_b(self):
        self.product.add_part("PartB2")

    def build_part_c(self):
        self.product.add_part("PartC2")

    def get_product(self):
        return self.product


class Director:
    def __init__(self):
        self.builder = None

    def set_builder(self, builder):
        self.builder = builder

    def build_minimum_viable_product(self):
        self.builder.build_part_a()

    def build_full_featured_product(self):
        self.builder.build_part_a()
        self.builder.build_part_b()
        self.builder.build_part_c()


if __name__ == "__main__":
    director = Director()

    builder1 = ConcreteBuilder1()
    director.set_builder(builder1)
    director.build_minimum_viable_product()
    product1 = builder1.get_product()
    print(product1.list_parts())

    builder2 = ConcreteBuilder2()
    director.set_builder(builder2)
    director.build_full_featured_product()
    product2 = builder2.get_product()
    print(product2.list_parts())
