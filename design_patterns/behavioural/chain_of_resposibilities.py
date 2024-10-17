"""
Avoids coupling the sender of a request to its receiver by giving more than one object a chance to handle the request.
Chain the receiving objects and pass the request along the chain until an object handles it.
"""


class Handler:
    def set_next(self, handler):
        pass

    def handle(self, request):
        pass


class AbstractHandler(Handler):
    _next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    def handle(self, request):
        if self._next_handler:
            return self._next_handler.handle(request)
        return None


class ConcreteHandler1(AbstractHandler):
    def handle(self, request):
        if request == "handler1":
            return "Handled by ConcreteHandler1"
        return super().handle(request)


class ConcreteHandler2(AbstractHandler):
    def handle(self, request):
        if request == "handler2":
            return "Handled by ConcreteHandler2"
        return super().handle(request)


if __name__ == "__main__":
    handler1 = ConcreteHandler1()
    handler2 = ConcreteHandler2()
    handler1.set_next(handler2)

    result1 = handler1.handle("handler1")
    print(result1)  # Handled by ConcreteHandler1

    result2 = handler1.handle("handler2")
    print(result2)  # Handled by ConcreteHandler2

    result3 = handler1.handle("handler3")
    print(result3)  # None
