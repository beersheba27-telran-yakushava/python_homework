from typing import Callable
from typing import Any, cast

def merge_in_place[T](
        items: list[T],
        start: int,
        len1: int,
        size: int ,
        key: Callable[[T], Any] | None = None
    ) -> None:
    """
    merges two sorted by key subparts in place of a list's part
    Time complexity O[N]
    Space complexity O[1] no additional list is created
    items - list of T objects (T any type generic at call time)
    start - start index of a being merged list
    len1 - length of the first subpart
    size - length of whole part
    Example: items - [3, 5, 7, -11, 0, 4, -10, -20, 100, -80,-4, 8 ], key - abs function
    start - 0; len1 - 4; size - 8
    call as  merge_in_place(items, start=0, len1=4, size=8, key=abs)
    updated itesms should be as [0, 3, 4, 5, 7, -10, -11, -20, 100, -80,-4, 8]
    """
    if not key: key = lambda x: cast(Any, x)
    i, j, end = start, start + len1, start + size

    while i < j and j < end:
        if key(items[j]) < key(items[i]):
            val = items[j]
            items[i + 1 : j + 1] = items[i:j]
            items[i] = val
            j += 1
        i += 1
