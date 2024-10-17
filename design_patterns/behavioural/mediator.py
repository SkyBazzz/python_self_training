"""

"""


class Colleague:
    def __init__(self, mediator):
        self._mediator = mediator


class ConcreteColleague1(Colleague):
    def send(self, message):
        self._mediator.send(message, self)

    def receive(self, message):
        return f"ConcreteColleague1 received message: {message}"


class ConcreteColleague2(Colleague):
    def send(self, message):
        self._mediator.send(message, self)

    def receive(self, message):
        return f"ConcreteColleague2 received message: {message}"


class Mediator:
    def add_colleague(self, colleague):
        pass

    def send(self, message, colleague):
        pass


class ConcreteMediator(Mediator):
    _colleagues = []

    def add_colleague(self, colleague):
        self._colleagues.append(colleague)

    def send(self, message, colleague):
        for c in self._colleagues:
            if c != colleague:
                print(c.receive(message))


if __name__ == "__main__":
    mediator = ConcreteMediator()

    colleague1 = ConcreteColleague1(mediator)
    colleague2 = ConcreteColleague2(mediator)

    mediator.add_colleague(colleague1)
    mediator.add_colleague(colleague2)

    colleague1.send("Hello from Colleague 1")
    # Output: ConcreteColleague2 received message: Hello from Colleague 1

    colleague2.send("Hello from Colleague 2")
    # Output: ConcreteColleague1 received message: Hello from Colleague 2
