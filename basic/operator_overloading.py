class Indexer:
    def __getitem__(self, item):
        return item**2


x = Indexer()
print(x[2], "| x[i] calls x.__getitem__")

for i in range(5):
    print(x[i], end=" ")
print("")
# Intercepting slices
l = [1, 2, 3, 4, 5, 6]
print(l[2:4])
print(l[2:])
print(l[:-2])
print(l[::-2])
print(l[slice(2, 4)])
print(l[slice(2, None)])
print(l[slice(None, -2)])
print(l[slice(None, None, -2)])


class Indexer:
    l = [1, 2, 3, 4, 5, 6]

    def __getitem__(self, item):
        print("getitem:", item)
        return self.l[item]

    def __setitem__(self, key, value):
        print("setitem:", key, value)
        self.l[key] = value

    def __str__(self):
        return str(self.l)


x = Indexer()
print(x[0])
print(x[1])
print(x[-1])
print(x[2:4])
print(x[2:])
print(x[:-2])
print(x[::-2])
x[0] = 11
print(x)


class Iters:
    """
    Example of __iter__, __next__, __contains__, __getitem__
    for boolean x in iterable - preferable is __contains__
    overall method execution is for runs __iter__, __iter__ runs __next__

    contains: True
    iter=> next:1 | next:2 | next:3 | next:4 | next:5 | next:
    iter=> next:next:next:next:next:next:[1, 4, 9, 16, 25]
    iter=> next:next:next:next:next:next:['0b1', '0b10', '0b11', '0b100', '0b101']

    Try comment one by one:
    1.) __contains__ => __next__ overtakes the run.

    iter=> next:next:next:True
    iter=> next:1 | next:2 | next:3 | next:4 | next:5 | next:
    iter=> next:next:next:next:next:next:[1, 4, 9, 16, 25]
    iter=> next:next:next:next:next:next:['0b1', '0b10', '0b11', '0b100', '0b101']

    2.) __iter__ => __getitem__ overtakes the run

    get[0]:get[1]:get[2]:True
    get[0]:1 | get[1]:2 | get[2]:3 | get[3]:4 | get[4]:5 | get[5]:
    get[0]:get[1]:get[2]:get[3]:get[4]:get[5]:[1, 4, 9, 16, 25]
    get[0]:get[1]:get[2]:get[3]:get[4]:get[5]:['0b1', '0b10', '0b11', '0b100', '0b101']


    """

    def __init__(self, value):
        self.data = value

    def __getitem__(self, item):
        print(f"get[{item}]:", end="")
        return self.data[item]

    def __iter__(self):
        print("iter=> ", end="")
        self.ix = 0
        return self

    def __next__(self):
        print("next:", end="")
        if self.ix == len(self.data):
            raise StopIteration
        item = self.data[self.ix]
        self.ix += 1
        return item

    def __contains__(self, item):
        print("contains: ", end="")
        return item in self.data


print("=" * 60)
X = Iters([1, 2, 3, 4, 5])
print(3 in X)
for i in X:
    print(i, end=" | ")
print()
print([i**2 for i in X])
print(list(map(bin, X)))

I = iter(X)
while True:
    try:
        print(next(I), end=" @ ")
    except StopIteration:
        break
print()
print("=" * 60)


class MyAttr:
    def __init__(self, name, surname) -> None:
        self.name = name
        self.surname = surname

    def __getattr__(self, item):
        return f"No attr {item}"

    def __getattribute__(self, item):
        if "name" in item:
            print("YOU ARE HERE")
        return super().__getattribute__(item)


my_attr = MyAttr("Olex", "Balk")
print(my_attr.name)
print(my_attr.surname)
print(my_attr.awesome)
print("=" * 60)

# Management Techniques Compared
print("dynamically computed attributes with properties")


class Powers:
    def __init__(self, square, cube):
        self._square = square
        self._cube = cube

    def get_square(self):
        return self._square**2

    def set_square(self, value):
        self._square = value

    square = property(get_square, set_square)

    def get_cube(self):
        return self._cube**3

    cube = property(get_cube)


X = Powers(3, 4)
print(X.square)
print(X.cube)
X.square = 5
print(X.square)

print("Same, but with descriptors")


class DescSquare:
    def __get__(self, instance, owner):
        return instance._square**2

    def __set__(self, instance, value):
        instance._square = value


class DescCube:
    def __get__(self, instance, owner):
        return instance._cube**3


class Powers:
    square = DescSquare()
    cube = DescCube()

    def __init__(self, square, cube):
        self._square = square
        self._cube = cube


X = Powers(3, 4)
print(X.square)
print(X.cube)
X.square = 5
print(X.square)

print("Same, but with generic __getattr__ undefined attribute interception")


class Powers:
    def __init__(self, square, cube):
        self._square = square
        self._cube = cube

    def __getattr__(self, name):
        if name == "square":
            return self._square**2
        elif name == "cube":
            return self._cube**3
        else:
            raise TypeError(f"unknown attr:{name}")

    def __setattr__(self, name, value):
        if name == "square":
            self.__dict__["_square"] = value
        else:
            self.__dict__[name] = value


X = Powers(3, 4)
print(X.square)
print(X.cube)
X.square = 5
print(X.square)

print("Same, but with generic __getattribute__ all attribute interception")


class Powers:
    def __init__(self, square, cube):
        self._square = square
        self._cube = cube

    def __getattribute__(self, name):
        if name == "square":
            return object.__getattribute__(self, "_square") ** 2
        elif name == "cube":
            return object.__getattribute__(self, "_cube") ** 3
        else:
            return object.__getattribute__(self, name)

    def __setattr__(self, name, value):
        if name == "square":
            self.__dict__["_square"] = value
        else:
            self.__dict__[name] = value


X = Powers(3, 4)
print(X.square)
print(X.cube)
X.square = 5
print(X.square)
