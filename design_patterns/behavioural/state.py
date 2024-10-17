"""
Allows an object to alter its behavior when its internal state changes. The object will appear to change its class.
"""


class State:
    def do_state(self):
        pass


class Context:
    def __init__(self, state):
        self.state = state

    def do_state(self):
        self.state.do_state()


class StateA(State):
    def do_state(self):
        print("State A")


class StateB(State):
    def do_state(self):
        print("State B")


if __name__ == "__main__":
    state_a = StateA()
    context = Context(state_a)
    context.do_state()  # Output: State A

    state_b = StateB()
    context.state = state_b
    context.do_state()  # Output: State B
