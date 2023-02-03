class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        print("fetch...", end="")
        return self._name

    def set_name(self, value):
        print("change...", end="")
        self._name = value

    def del_name(self):
        print("remove...", end="")
        del self._name

    name = property(get_name, set_name, del_name, "name property docs")


bot = Person("Jenkins")
print(bot.name)
bot.name = "Jenkins2"
print(bot.name)

del bot.name

print(f"\n{'-' * 20}")
sue = Person("Sue Jones")
print(sue.name)
print(Person.name.__doc__)


class PropSquare:
    def __init__(self, start):
        self.value = start

    def get_x(self):
        return self.value**2

    def set_x(self, value):
        self.value = value

    X = property(get_x, set_x)


P = PropSquare(3)
Q = PropSquare(32)

print(P.X)
P.X = 4
print(P.X)
print(Q.X)


class PersonDecorator:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        """name getter docs"""
        print("fetch...", end="")
        return self._name

    @name.setter
    def name(self, value):
        """name setter docs"""
        print("change...", end="")
        self._name = value

    @name.deleter
    def name(self):
        """name del docs"""
        print("remove...", end="")
        del self._name


bom = PersonDecorator("Stuart")
print(bom.name)
bom.name = "Jenkins2"
print(bom.name)

del bom.name

print(f"\n{'-' * 20}")
sau = PersonDecorator("Sum Jones")
print(sau.name)
print(PersonDecorator.name.__doc__)
print(PersonDecorator.name.getter.__doc__)
print(PersonDecorator.name.setter.__doc__)
print(PersonDecorator.name.deleter.__doc__)
print("Attributes validation")


class CardHolder:
    acct_len = 8
    retire_age = 59.5

    def __init__(self, acct, name, age, address) -> None:
        self.acct = acct
        self.name = name
        self.age = age
        self.address = address

    def get_name(self):
        return self._name

    def set_name(self, value: str):
        value = value.lower().replace(" ", "_")
        self._name = value

    name = property(get_name, set_name)

    def get_age(self):
        return self._age

    def set_age(self, value):
        if 0 < value > 150:
            raise ValueError("value not in range 0 - 150")
        else:
            self._age = value

    age = property(get_age, set_age)

    def get_acct(self):
        return f"{self.__acct[:-3]}***"

    def set_acct(self, value):
        value = value.replace("-", "")
        if len(value) != self.acct_len:
            raise TypeError("invalid acct number")
        else:
            self.__acct = value

    acct = property(get_acct, set_acct)

    def remain_get(self):
        return self.retire_age - self.age

    remain = property(remain_get)


bob = CardHolder("1234-5678", "Bob Smith", 40, "123 main st")
print(bob.acct, bob.name, bob.age, bob.remain, bob.address, sep=" / ")
bob.name = "Bob Q. Smith"
bob.age = 50
bob.acct = "23-45-67-89"
print(bob.acct, bob.name, bob.age, bob.remain, bob.address, sep=" / ")
sue = CardHolder("5678-12-34", "Sue Jones", 35, "124 main st")
print(sue.acct, sue.name, sue.age, sue.remain, sue.address, sep=" / ")
try:
    sue.age = 200
except:
    print("Bad age for Sue")
try:
    sue.remain = 5
except:
    print("Can't set sue.remain")
try:
    sue.acct = "1234567"
except:
    print("Bad acct for Sue")

print("Here must be example with Descriptors, but it's missing")
print("Validation with __getattr__")


class CardHolder:
    acctlen = 8
    retireage = 59.5

    def __init__(self, acct, name, age, addr):
        self.acct = acct
        self.name = name
        self.age = age
        self.address = addr

    def __getattr__(self, name):
        if name == "acct":
            return f"{self._acct[:-3]}***"
        elif name == "remain":
            return self.retireage - self.age
        else:
            raise AttributeError(name)

    def __setattr__(self, name, value):
        if name == "name":
            value = value.lower().replace(" ", "_")
        elif name == "age":
            if value < 0 or value > 150:
                raise ValueError("invalid age")
        elif name == "acct":
            name = "_acct"
            value = value.replace("-", "")
            if len(value) != self.acctlen:
                raise TypeError("invalid acct number")
        elif name == "remain":
            raise TypeError("cannot set remain")
        self.__dict__[name] = value


bob = CardHolder("1234-5678", "Bob Smith", 40, "123 main st")
print(bob.acct, bob.name, bob.age, bob.remain, bob.address, sep=" / ")
bob.name = "Bob Q. Smith"
bob.age = 50
bob.acct = "23-45-67-89"
print(bob.acct, bob.name, bob.age, bob.remain, bob.address, sep=" / ")
sue = CardHolder("5678-12-34", "Sue Jones", 35, "124 main st")
print(sue.acct, sue.name, sue.age, sue.remain, sue.address, sep=" / ")
try:
    sue.age = 200
except:
    print("Bad age for Sue")
try:
    sue.remain = 5
except:
    print("Can't set sue.remain")
try:
    sue.acct = "1234567"
except:
    print("Bad acct for Sue")
print(sue.acct)
print(sue._acct)
