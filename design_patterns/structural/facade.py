"""
This pattern provides a simple interface to a complex system of classes, libraries, or frameworks.
"""


class SubsystemA:
    def operation_a1(self):
        return "Subsystem A: Operation A1"

    def operation_a2(self):
        return "Subsystem A: Operation A2"


class SubsystemB:
    def operation_b1(self):
        return "Subsystem B: Operation B1"

    def operation_b2(self):
        return "Subsystem B: Operation B2"


class Facade:
    def __init__(self, subsystem_aa, subsystem_bb):
        self._subsystem_a = subsystem_aa
        self._subsystem_b = subsystem_bb

    def operation(self):
        res = []
        res.append(self._subsystem_a.operation_a1())
        res.append(self._subsystem_b.operation_b1())
        res.append(self._subsystem_a.operation_a2())
        res.append(self._subsystem_b.operation_b2())
        return "\n".join(res)


if __name__ == "__main__":
    subsystem_a = SubsystemA()
    subsystem_b = SubsystemB()
    facade = Facade(subsystem_a, subsystem_b)

    RESULT = facade.operation()
    print(RESULT)
