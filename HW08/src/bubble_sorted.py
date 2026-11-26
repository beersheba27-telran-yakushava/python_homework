from collections.abc import Callable, Sequence
from typing import Any, TypeVar, cast

T = TypeVar("T")

def bubble_sorted(
    items: Sequence[T],
    key: Callable[[T], Any] | None = None,
) -> list[T]:
    """
    Sequence[object] means immutable list, so items cannot be updated
    returns new list of objects sorted using algorithm "bubble sort"
    in accorgance with key function-converter like standard Python sorting 
    items - sequence of any objects
    key - a function taking one object and returning converted object having standard operator ">"
    default value None designating standard Python sorting with no converting initial object
    For example, bubble_sort(numbers) - regular sort of numbers 
    bubble_sort(numbers, abs) - sort of numbers in accordance with their abs values
    Unlike the standard sorting methods of Python, the function may be called with no explicit specifying key=                
    """
    result: list[T] = list(items)
    key_func: Callable[[T], Any] = (key if key is not None else lambda x: cast(Any, x))

    unsorted_end: int = len(result) - 1
    swapped: bool = True

    while unsorted_end > 0 and swapped:
        swapped = False
        for j in range(unsorted_end):
            if key_func(result[j]) > key_func(result[j + 1]):
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        unsorted_end -= 1

    return result
