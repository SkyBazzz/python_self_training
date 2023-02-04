def solution(n):
    roman = {
        1: "I",
        4: "IV",
        5: "V",
        9: "IX",
        10: "X",
        40: "XL",
        50: "L",
        90: "XC",
        100: "C",
        400: "CD",
        500: "D",
        900: "CM",
        1000: "M",
    }
    result = ""

    sorted_roman = sorted(roman, reverse=True)

    for roman_int in sorted_roman:
        while n >= roman_int:
            result += roman[roman_int]
            n -= roman_int

    return result


if __name__ == "__main__":
    assert solution(1) == "I"
    assert solution(4) == "IV"
    assert solution(6) == "VI"
    assert solution(14) == "XIV"
    assert solution(21) == "XXI"
    assert solution(89) == "LXXXIX"
    assert solution(91) == "XCI"
