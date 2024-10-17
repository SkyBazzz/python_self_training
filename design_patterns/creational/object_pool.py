"""
The Object Pool Pattern allows objects to be reused instead of creating new objects when they are needed.
This can improve performance and reduce memory usage.
"""


class ObjectPool:
    def __init__(self, object_class, size):
        self.object_class = object_class
        self.size = size
        self.objects = [self.object_class() for _ in range(self.size)]

    def acquire(self):
        return self.objects.pop() if self.objects else self.object_class()

    def release(self, obj):
        self.objects.append(obj)


class PooledObject:
    def __init__(self):
        self.property = None

    def use(self):
        self.property = "Used"

    def reset(self):
        self.property = None


if __name__ == "__main__":
    pool = ObjectPool(PooledObject, 2)

    obj1 = pool.acquire()
    obj1.use()
    print(obj1.property)  # Used

    obj2 = pool.acquire()
    obj2.use()
    print(obj2.property)  # Used

    pool.release(obj1)
    pool.release(obj2)

    obj3 = pool.acquire()
    print(obj3.property)  # None
