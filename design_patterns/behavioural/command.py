"""
Encapsulates a request as an object, thereby letting you parameterize clients with different requests,
queue or log requests, and support undoable operations.
"""


class BaseInvoker:
    def __init__(self):
        self._command = None

    def __str__(self):
        return "Hello it's Invoker"


class Invoker(BaseInvoker):
    def set_command(self, command):
        self._command = command

    def execute(self):
        return self._command.execute()


class Command:
    def execute(self):
        pass


class ConcreteCommand1(Command):
    def execute(self):
        return "Command 1"


class ConcreteCommand2(Command):
    def execute(self):
        return "Command 2"


# Client code
if __name__ == "__main__":
    invoker = Invoker()
    command1 = ConcreteCommand1()
    command2 = ConcreteCommand2()

    invoker.set_command(command1)
    result1 = invoker.execute()
    print(result1)  # Command 1

    invoker.set_command(command2)
    result2 = invoker.execute()
    print(result2)  # Command 2
