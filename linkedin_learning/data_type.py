class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        """
        Accepts an item as a parameter and appends it to the end of the list.

        The runtime for this method is O(1), or constant time, because appending to the end of the list
        happens in constant time.

        :param item: any
        :return: nothing
        """
        self.items.append(item)

    def pop(self):
        """
        Removes and returns the last item from the list, which is also the top item of the Stack.

        The runtime here is O(1) or constant time, because all it does is index to the last item of the list.

        :return: last item of the list
        """
        return self.items.pop() if self.items else None

    def peek(self):
        """
        Returns the last item of the list, which is also the top item of the Stack.

        The runtime here is O(1) or constant time, because all it does is index to the last item of the list.
        :return: last item
        """
        return self.items[-1] if self.items else None

    def size(self):
        """
        Returns the size of the list, which is also a size of the Stack.

        The runtime of finding the list is constant time, because finding the length of the list
        is also a constant time.
        :return: int size
        """
        return len(self.items)

    def is_empty(self):
        """
        Returns a Boolean value describing whether or not the Stack is empty.

        Testing for equality happens in a constant time.
        :return:
        """
        return self.items == []


def match_symbols(symbols: str):
    symbol_pairs = {"(": ")", "[": "]", "{": "}"}

    openers = symbol_pairs.keys()
    my_stack = Stack()

    index = 0
    while index < len(symbols):
        symbol = symbols[index]
        if symbol in openers:
            my_stack.push(symbol)
        else:  # Symbol is closer.

            # If the Stack is already empty, the symbols are not balanced.
            if my_stack.is_empty():
                return False

            # If there are still items in the Stack, check for a mis-match.
            else:
                top_item = my_stack.pop()
                if symbol != symbol_pairs[top_item]:
                    return False

        index += 1

    if my_stack.is_empty():
        return True
    return False


# True
print(match_symbols("((())){{{}}}"))
# False
print(match_symbols("{((}())){{{}}}"))


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """
        Accepts an item as a parameter and appends it to the beginning of the list.

        The runtime for this method is O(n), or linear time, because inserting to the beginning of the list
        forces all items of the list to move right.

        :param item: any
        :return: nothing
        """
        self.items.insert(item, 0)

    def dequeue(self):
        """
        Removes and returns the last item from the list, which is also the top item of the Queue.

        The runtime here is O(1) or constant time, because all it does is index to the last item of the list.

        :return: last item of the list
        """
        return self.items.pop() if self.items else None

    def peek(self):
        """
        Returns the last item of the list, which is also the top item of the Queue.

        The runtime here is O(1) or constant time, because all it does is index to the last item of the list.
        :return: last item
        """
        return self.items[-1] if self.items else None

    def size(self):
        """
        Returns the size of the list, which is also a size of the Queue.

        The runtime of finding the list is constant time, because finding the length of the list
        is also a constant time.
        :return: int size
        """
        return len(self.items)

    def is_empty(self):
        """
        Returns a Boolean value describing whether or not the Stack is empty.

        Testing for equality happens in a constant time.
        :return:
        """
        return self.items == []
