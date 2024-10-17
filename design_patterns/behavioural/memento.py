"""
Without violating encapsulation, captures and externalizes an object's internal state
so that the object can be restored to this state later.
"""


class Originator:
    def __init__(self, state):
        self._state = state

    def create_memento(self):
        return Memento(self._state)

    def restore(self, memento):
        self._state = memento.state

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value


class Memento:
    def __init__(self, state):
        self._state = state

    @property
    def state(self):
        return self._state


class Caretaker:
    def __init__(self, originatore):
        self._mementos = []
        self._originator = originatore

    def backup(self):
        self._mementos.append(self._originator.create_memento())

    def undo(self):
        if not self._mementos:
            return

        memento = self._mementos.pop()
        self._originator.restore(memento)


if __name__ == "__main__":
    originator = Originator("Initial state")
    print(f"Current state: {originator.state}")  # Output: Current state: Initial state

    caretaker = Caretaker(originator)
    caretaker.backup()

    originator.state = "State 1"
    print(f"Current state: {originator.state}")  # Output: Current state: State 1

    caretaker.backup()

    originator.state = "State 2"
    print(f"Current state: {originator.state}")  # Output: Current state: State 2

    caretaker.undo()
    print(f"Current state: {originator.state}")  # Output: Current state: State 1

    caretaker.undo()
    print(f"Current state: {originator.state}")  # Output: Current state: Initial state
