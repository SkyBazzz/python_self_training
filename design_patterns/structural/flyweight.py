"""
This pattern minimizes memory usage by sharing as much data as possible between similar objects.
"""


class Flyweight:
    def operation(self, extrinsic_state):
        pass


class ConcreteFlyweight(Flyweight):
    def __init__(self, intrinsic_state):
        self.intrinsic_state = intrinsic_state

    def operation(self, extrinsic_state):
        print(f"ConcreteFlyweight: Intrinsic state - {self.intrinsic_state}; Extrinsic state - {extrinsic_state}")


class FlyweightFactory:
    def __init__(self):
        self.flyweights = {}

    def get_flyweight(self, intrinsic_state):
        if intrinsic_state not in self.flyweights:
            self.flyweights[intrinsic_state] = ConcreteFlyweight(intrinsic_state)
        return self.flyweights[intrinsic_state]


if __name__ == "__main__":
    flyweight_factory = FlyweightFactory()

    flyweight_a = flyweight_factory.get_flyweight("A")
    flyweight_a.operation("1")  # ConcreteFlyweight: Intrinsic state - A; Extrinsic state - 1

    flyweight_b = flyweight_factory.get_flyweight("B")
    flyweight_b.operation("2")  # ConcreteFlyweight: Intrinsic state - B; Extrinsic state - 2

    flyweight_c = flyweight_factory.get_flyweight("A")
    flyweight_c.operation("3")  # ConcreteFlyweight: Intrinsic state - A; Extrinsic state - 3
