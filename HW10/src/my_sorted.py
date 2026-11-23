from collections.abc import Callable, Sequence
from math import sqrt

from HW8.src.bubble_sorted import bubble_sorted
from HW8.src.merge import merge

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
    parts: list[list[T]] = []

    for i in range(0, n, chunk_size):
        if n - i < chunk_size and parts:
            parts[-1].extend(items[i:])
            break
        parts.append(list(items[i : i + chunk_size]))

    sorted_parts = [bubble_sorted(part, key=key) for part in parts]

    merged: list[T] = sorted_parts[0]
    for part in sorted_parts[1:]:
        merged = merge(merged, part, key=key)

    return merged
