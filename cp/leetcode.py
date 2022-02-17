import math
from typing import List
import re
import integer as integer


def twoSum(nums: List[int], target: int) -> List[int]:
    """
    Two sum

    :param nums: Given an array of integers
    :param target: an integer target
    :return: indices of the two numbers such that they add up to target
    """

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


def reverse(x: int) -> int:
    """
    Reverse Integer

    :param x: 32-bit integer
    :return: x's digits reversed. If reversing x causes the value to go outside
    the signed 32-bit integer range [-231, 231 - 1], then return 0.
    """

    max_value = math.pow(2, 31) - 1
    min_value = math.pow(-2, 31)
    if min_value >= x or x >= max_value:
        return 0
    else:
        string_x = str(x)
        if x >= 0:
            rev_str = string_x[::-1]
        else:
            str_abs = string_x[1:]
            rev_str_abs = str_abs[::-1]
            rev_str = "-" + rev_str_abs
        rev_int = int(rev_str)
        if min_value >= rev_int or rev_int >= max_value:
            return 0
        else:
            return rev_int


def reverse2(x: int) -> int:
    max_value = math.pow(2, 31) - 1
    min_value = math.pow(-2, 31)

    n = (int(str(x)[::-1])) if x >= 0 else -(int(str(x * -1)[::-1]))
    return n if min_value <= n <= max_value else 0


def isPalindrome(x: int) -> bool:
    """
    Palindrome Number

    :param x: given an integer value
    :return: is palindrome
    """
    if x < 0:
        return False
    else:
        str_x = str(x)
        for i in range(math.floor(len(str_x) / 2)):
            if str_x[i] != str_x[-i - 1]:
                return False
        return True


def romanToInt(s: str) -> int:
    """
    Roman to Integer

    :param s: input Roman numeral
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
    converted_s = list()
    flag = False
    for index, roman_numeral in enumerate(s):
        if index != len(s) - 1:
            if (
                roman_numeral in six_subsractions
                and not flag
                and s[index + 1] in six_subsractions[s[index]]
            ):
                converted_s.append(roman_numeral + s[index + 1])
                flag = True
            elif not flag:
                converted_s.append(roman_numeral)
            else:
                flag = False
        elif not flag:
            converted_s.append(roman_numeral)

    roman_integer = 0
    for i in converted_s:
        if len(i) == 1:
            roman_integer += roman_numeral_to_integer[i]
        else:
            for minus in six_subsractions:
                if i[0] == minus:
                    roman_integer += (
                        roman_numeral_to_integer[i[1]] - roman_numeral_to_integer[i[0]]
                    )
                    break
    return roman_integer


def romanToInt1(s: str) -> int:
    rd = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    n = len(s)
    num = rd[s[n - 1]]
    for i in range(n - 2, -1, -1):
        if rd[s[i]] >= rd[s[i + 1]]:
            num += rd[s[i]]
        else:
            num -= rd[s[i]]
    return num


def longestCommonPrefix(strs: List[str]) -> str:
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


print(longestCommonPrefix(["flower", "flow", "flight"]))


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

    result = []
    for i in range(len(nums)):
        result.append(sum(nums[:i]) + nums[i])
    return result


print(running_sum([1, 2, 3, 4, 5]))
