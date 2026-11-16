from collections.abc import Callable, Sequence
from typing import Any, TypeVar, cast

T = TypeVar("T")

def merge(
    part1: Sequence[T],
    part2: Sequence[T],
    key: Callable[[T], Any] | None = None,
) -> list[T]:
    """
    part1 and part2 -  sorted in accordance with key function-converter lists of any objects 
    key - a function taking one object and returning converted object having standard operator ">"
    default value None designating standard Python sorting with no converting initial objects
    returns new list, sorted in accordance with key function-converter, comprising of two lists-parts 
    For example, merge([-11, 3, 5, 7], [-20, -10, 0, 4])  => [-20, -11, -10, 0, 3, 4, 5, 7]
    merge([3, 5, 7, -11 ], [ 0, 4, -10, -20 ], abs)  => [ 0, 3, 4, 5, 7, -10, -11,-20]
    """
    key_func: Callable[[T], Any] = (key if key is not None else lambda x: cast(Any, x))

    result: list[T] = []
    i, j = 0, 0
    len1, len2 = len(part1), len(part2)

    while i < len1 and j < len2:
        if key_func(part1[i]) > key_func(part2[j]):
            result.append(part2[j])
            j += 1
        else:
            result.append(part1[i])
            i += 1

    result.extend(part1[i:])
    result.extend(part2[j:])

    return result
