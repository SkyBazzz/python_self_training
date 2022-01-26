def array(string: str):
    return ' '.join(string.split(',')[1:-1]) or None


def sum_3_5(number: int):
    threes = (number - 1) // 3
    fives = (number - 1) // 5
    fifteens = (number - 1) // 15
    return 3 * threes * (threes + 1) // 2 + 5 * fives * (fives + 1) // 2 - 15 * fifteens * (fifteens + 1) // 2


def next_pal(val: int):
    new_value = val + 1
    while str(new_value) != str(new_value)[::-1]:
        new_value += 1
    return new_value


def center(word: str, width, fill=' '):
    pad, odd = divmod(width - len(word), 2)
    return f"{fill * (pad + odd)}{word}{fill * pad}"


def become_compiler(s1: str, s2: str):
    s1 = sum(s1.encode())
    s2 = sum(s2.encode())
    return s1 + s2


def sort_my_string(word: str):
    return f'{word[::2]} {word[1::2]}'


def sum_two_smallest_numbers(numbers: list):
    return sum(sorted(numbers)[:2])


print(sum_two_smallest_numbers([5, 8, 12, 18, 22]))
