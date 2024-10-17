"""
Defines a representation for its grammar along with an interpreter
that uses the representation to interpret sentences in the language.
"""


class Context:
    def __init__(self):
        self.variables = {}

    def __str__(self):
        return "Context"


class AbstractExpression:
    def interpret(self, contexte):
        pass


class Variable(AbstractExpression):
    def __init__(self, name):
        self.name = name

    def interpret(self, contexte):
        if self.name not in contexte.variables:
            raise ValueError(f"Variable {self.name} not found")
        return contexte.variables[self.name]


class Constant(AbstractExpression):
    def __init__(self, value):
        self.value = value

    def interpret(self, contexte):
        return self.value


class Add(AbstractExpression):
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def interpret(self, contexte):
        return self.left.interpret(contexte) + self.right.interpret(contexte)


# Client code
if __name__ == "__main__":
    context = Context()
    context.variables["x"] = 5
    context.variables["y"] = 10

    expr1 = Add(Variable("x"), Constant(5))
    result1 = expr1.interpret(context)
    print(result1)  # 10

    expr2 = Add(Variable("x"), Variable("y"))
    result2 = expr2.interpret(context)
    print(result2)  # 15
