import math
from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    Two sum

    :param nums: Given an array of integers
    :param target: an integer target
    :return: indices of the two numbers such that they add up to target
    """

    for integer in nums:
        for another_integer in range(integer + 1, len(nums)):
            if nums[integer] + nums[another_integer] == target:
                return [integer, another_integer]
    return []


def reverse(value_x: int) -> int:
    """
    Reverse Integer

    :param value_x: 32-bit integer
    :return: x's digits reversed. If reversing x causes the value to go outside
    the signed 32-bit integer range [-231, 231 - 1], then return 0.
    """

    max_value = math.pow(2, 31) - 1
    min_value = math.pow(-2, 31)
    if min_value >= value_x or value_x >= max_value:
        return 0
    string_x = str(value_x)
    if value_x >= 0:
        rev_str = string_x[::-1]
    else:
        str_abs = string_x[1:]
        rev_str_abs = str_abs[::-1]
        rev_str = f"-{rev_str_abs}"
    rev_int = int(rev_str)
    return 0 if min_value >= rev_int or rev_int >= max_value else rev_int


def reverse2(value_x: int) -> int:
    max_value = math.pow(2, 31) - 1
    min_value = math.pow(-2, 31)

    number = (int(str(value_x)[::-1])) if value_x >= 0 else -(int(str(value_x * -1)[::-1]))
    return number if min_value <= number <= max_value else 0


def is_palindrome(value_x: int) -> bool:
    """
    Palindrome Number

    :param value_x: given an integer value
    :return: is palindrome
    """
    if value_x < 0:
        return False
    str_x = str(value_x)
    return all(str_x[integer] == str_x[-integer - 1] for integer in range(math.floor(len(str_x) / 2)))


def roman_to_int(value_s: str) -> int:
    """
    Roman to Integer

    :param value_s: input Roman numeral
    :return: converted to an integer
    """
    roman_numeral_to_integer = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }
    six_subsractions = {"I": ["V", "X"], "X": ["L", "C"], "C": ["D", "M"]}
    converted_s = []
    flag = False
    for index, roman_numeral in enumerate(value_s):
        if index != len(value_s) - 1:
            if (
                roman_numeral in six_subsractions
                and not flag
                and value_s[index + 1] in six_subsractions[value_s[index]]
            ):
                converted_s.append(roman_numeral + value_s[index + 1])
                flag = True
            elif not flag:
                converted_s.append(roman_numeral)
            else:
                flag = False
        elif not flag:
            converted_s.append(roman_numeral)

    roman_integer = 0
    for integer in converted_s:
        if len(integer) == 1:
            roman_integer += roman_numeral_to_integer[integer]
        else:
            for minus in six_subsractions:
                if integer[0] == minus:
                    roman_integer += roman_numeral_to_integer[integer[1]] - roman_numeral_to_integer[integer[0]]
                    break
    return roman_integer


def roman_to_int1(value_s: str) -> int:
    roman_numbers = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    length = len(value_s)
    num = roman_numbers[value_s[length - 1]]
    for integer in range(length - 2, -1, -1):
        if roman_numbers[value_s[integer]] >= roman_numbers[value_s[integer + 1]]:
            num += roman_numbers[value_s[integer]]
        else:
            num -= roman_numbers[value_s[integer]]
    return num


def longest_common_prefix(strs: List[str]) -> str:
    """
    14. Longest Common Prefix
    :param strs: List of str
    :return: common prefix
    """
    prefix = strs[0]
    for word in strs:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix


print(longest_common_prefix(["flower", "flow", "flight"]))


def maximum_wealth(accounts):
    """
    :type accounts: List[List[int]]
    :rtype: int
    """
    return max(map(sum, accounts))


print(maximum_wealth([[1, 2, 3, 4, 5], [2, 3, 4, 5, 6]]))


def running_sum(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """

    return [sum(nums[:integer]) + integer for integer in nums]


print(running_sum([1, 2, 3, 4, 5]))
