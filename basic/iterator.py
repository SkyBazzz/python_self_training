class Range:
    def __init__(self, start, finish, step) -> None:
        self.start = start
        self.finish = finish
        self.step = step
        self.current_number = self.start

    def __iter__(self):
        self.current_number = self.start
        return self

    def __next__(self):
        if self.step > 0 and self.current_number >= self.finish:
            raise StopIteration
        elif self.step < 0 and self.current_number <= self.finish:
            raise StopIteration

        number_to_return = self.current_number
        self.current_number += self.step
        return number_to_return


my_range = Range(-1, -5, -1)

for i in my_range:
    print(i)
