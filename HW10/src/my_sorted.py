from collections.abc import Callable, Sequence
from math import sqrt

from HW08.src.bubble_sorted import bubble_sorted
from HW08.src.merge import merge

def my_sorted[T, K](items: Sequence[T], /, *, key:Callable[[T], T|K]|None=None) -> list[T]:
    """
    returns sorted by key list
    implementation according the following algorithm:
    "items" is divided on the parts, each of which contains sqrt(len(items)) items
    Each part should be sorted separately by bubble sorting algorithm that you have already implemented
    After that all parts should be merged.
    No limitations for extra space
    Note: To use "sqrt" function from the module "math". This function returns float type
    so you should apply function "int" and the last part may contain more items
    """
    n = len(items)
    if n <= 1: return list(items)

    chunk_size = int(sqrt(n))
    parts = [
        list(items[i * chunk_size : (i + 1) * chunk_size])
        for i in range(chunk_size - 1)
    ]
    parts.append(list(items[(chunk_size - 1) * chunk_size :]))

    sorted_parts = [bubble_sorted(part, key=key) for part in parts]

    merged: list[T] = sorted_parts[0]
    for part in sorted_parts[1:]:
        merged = merge(merged, part, key=key)

    return merged
