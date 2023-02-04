from typing import List


def array_diff(a: List[int], b: List[int]):
    return [i for i in a if i not in b]
