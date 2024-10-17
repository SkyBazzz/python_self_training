"""
Defines a family of algorithms, encapsulates each one, and makes them interchangeable at runtime.
It lets the algorithm vary independently of clients that use it.
"""

from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def do_operation(self, num1, num2):
        pass


class AddStrategy(Strategy):
    def do_operation(self, num1, num2):
        return num1 + num2


class SubtractStrategy(Strategy):
    def do_operation(self, num1, num2):
        return num1 - num2


class Context:
    def __init__(self, strategy):
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def execute_strategy(self, num1, num2):
        return self._strategy.do_operation(num1, num2)


# Client code
if __name__ == "__main__":
    context = Context(AddStrategy())
    print("Addition:", context.execute_strategy(10, 5))  # Output: Addition: 15

    context.set_strategy(SubtractStrategy())
    print("Subtraction:", context.execute_strategy(10, 5))  # Output: Subtraction: 5
