from collections.abc import Callable, Sequence
from typing import Any, cast
from itertools import batched

from HW08.src.merge import merge

def my_sorted[T, K](items: Sequence[T], /, *, key: Callable[[T], T|K]|None = None) -> list[T]:
    """
    returns sorted by key list
    implementation according the following algorithm:
    1. Creating list of already sorted by key parts from "items"
    (no additional sorting is required)
    2. Merge of all parts from the created above list
    """
    if len(items) <= 1: return list(items)
    if key is None: key = lambda x: cast(Any, x)

    parts = _split_into_sorted_parts(items, key)

    return _merge_all_parts(parts, key)

def _split_into_sorted_parts[T](items: Sequence[T], key: Callable[[T], Any]) -> list[list[T]]:
    parts: list[list[T]] = []
    start = 0

    for i in range(1, len(items)):
        if key(items[i]) < key(items[i - 1]):
            parts.append(list(items[start:i]))
            start = i

    parts.append(list(items[start:]))
    return parts

def _merge_all_parts[T](parts: list[list[T]], key: Callable[[T], Any]) -> list[T]:
    while len(parts) > 1:
        parts = [
            merge(pair[0], pair[1], key) if len(pair) == 2 else pair[0]
            for pair in batched(parts, 2)
        ]

    return parts[0]
