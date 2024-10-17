"""
Defines the skeleton of an algorithm in a method, deferring some steps to subclasses.
Template Method lets subclasses redefine certain steps of an algorithm without changing the algorithm's structure.
"""

from abc import ABC, abstractmethod


class AbstractClass(ABC):
    def template_method(self):
        self._step_1()
        self._step_2()

    @abstractmethod
    def _step_1(self):
        pass

    @abstractmethod
    def _step_2(self):
        pass


class ConcreteClassA(AbstractClass):
    def _step_1(self):
        print("ConcreteClassA: Step 1")

    def _step_2(self):
        print("ConcreteClassA: Step 2")


class ConcreteClassB(AbstractClass):
    def _step_1(self):
        print("ConcreteClassB: Step 1")

    def _step_2(self):
        print("ConcreteClassB: Step 2")


if __name__ == "__main__":
    a = ConcreteClassA()
    a.template_method()
    # Output:
    # ConcreteClassA: Step 1
    # ConcreteClassA: Step 2

    b = ConcreteClassB()
    b.template_method()
    # Output:
    # ConcreteClassB: Step 1
    # ConcreteClassB: Step 2
