from bisect import bisect_left
from collections.abc import Sequence

def get_all_not_in_range(numbers: Sequence[int], disallowed: range) -> list[int] :
    """
    numbers - sorted list of numbers in ascending order 
    disallowed - range of numbers (may be empty)
    returns list of numbers from "numbers" that are not in a given range
    """
    if not disallowed:
        return list(numbers)

    left = bisect_left(numbers, disallowed.start)
    right = bisect_left(numbers, disallowed.stop)

    return list(numbers[:left]) + list(numbers[right:])
