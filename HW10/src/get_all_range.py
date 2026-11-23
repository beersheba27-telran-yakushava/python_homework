from bisect import bisect_left
from collections.abc import Sequence

def get_all_range(numbers: Sequence[int], allowed: range|None = None) -> list[int]:
    """
    numbers - sorted list of numbers in ascending order
    allowed - range of numbers (may be empty)
    returns list of numbers that greater or equal minimal value of range and less than maximal value 
    for empty range the function returns the empty list
    for missed second argument the function returns the same "numbers"
    """
    if allowed is None:
        return list(numbers)

    if not allowed:
        return []

    left = bisect_left(numbers, allowed.start)
    right = bisect_left(numbers, allowed.stop)

    return list(numbers[left:right])
