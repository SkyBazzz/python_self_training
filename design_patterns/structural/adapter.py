"""
This pattern allows two incompatible interfaces to work together by wrapping an object
that has one interface with another object that has a compatible interface.
"""


class Target:
    def request(self):
        pass


class Adaptee:
    def specific_request(self):
        print("Adaptee: Handling specific request")


class Adapter(Target):
    def __init__(self, adapteee):
        self.adaptee = adapteee

    def request(self):
        print("Adapter: Converting request to specific request")
        self.adaptee.specific_request()


if __name__ == "__main__":
    adaptee = Adaptee()
    adapter = Adapter(adaptee)

    adapter.request()
