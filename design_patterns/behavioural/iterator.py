"""
Provides a way to access the elements of an aggregate object sequentially
without exposing its underlying representation.
"""


class Iterator:
    def __init__(self, collectione):
        self._collection = collectione
        self._index = 0

    def __next__(self):
        if self._index < len(self._collection):
            result = self._collection[self._index]
            self._index += 1
            return result
        raise StopIteration


class Collection:
    def __init__(self):
        self._items = []

    def add_item(self, iteme):
        self._items.append(iteme)

    def __iter__(self):
        return Iterator(self._items)


# Client code
if __name__ == "__main__":
    collection = Collection()
    collection.add_item("item 1")
    collection.add_item("item 2")
    collection.add_item("item 3")

    for item in collection:
        print(item)
