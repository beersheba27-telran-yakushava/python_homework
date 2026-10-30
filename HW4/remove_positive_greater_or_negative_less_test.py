import pytest
from remove_positive_greater_or_negative_less import remove_positive_greater_or_negative_less

@pytest.mark.parametrize("numbers, positive_lim, negative_lim, expected", [
    ([1, 2, 11, -3, 10, 15], 10, -3, [1, 2, -3, 10]),
    ([20, 30, -10, -15], 10, -5, []),
    ([5, 8, -2, -4, 0], 10, -5, [5, 8, -2, -4, 0]),
    ([10, -3], 10, -3, [10, -3]),
    ([], 10, -3, []),
    ([0, 0, 0], 5, -5, [0, 0, 0]),
    ([-1, -2, -10, -20], 5, -5, [-1, -2]),
    ([1, 2, 10, 20], 5, -5, [1, 2])
])

def test_remove_positive_greater_or_negative_less(numbers: list[int], positive_lim: int, negative_lim: int, expected: list[int]):
    assert remove_positive_greater_or_negative_less(numbers, positive_lim, negative_lim) == expected
