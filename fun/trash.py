from math import floor


def fib(n):
    """
    # 1 1 2 3 5
    :param n - sequence of n numbers
    :return: n-th number
    """
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


print(fib(3))


def is_palindrome(word: str):
    """
    Returns true if the input single word is palindrome
    :param word: word
    :return: true if palindrome
    """
    for i in range(floor(len(word) / 2)):
        if word[i] != word[-i - 1]:
            return False
    return True


print(is_palindrome("catac"))
print(is_palindrome("cat"))
print(is_palindrome("catac"))
