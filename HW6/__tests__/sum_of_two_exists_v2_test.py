import pytest
from HW6.src.sum_of_two_exists import sum_of_two_exists

@pytest.mark.parametrize("numbers, target_sum, expected", [
    ([1, -1, 40, 50, 0], 0, True),
    ([1, -1, 40, 50, 0], 42, False),
    ([5, 10, 15], 20, True),
    ([5, 10, 15], 10, False),
    ([5, 5, 15], 10, True),
    ([], 10, False),
    ([10], 10, False),
    ([5, 5], 10, True),
    ([5, 6], 10, False),
    ([-10, -20, 30], -30, True),
    ([0, 0], 0, True),
    ([0, 5], 0, False),
    ([1000000, -1000000], 0, True)
])

def test_sum_of_two_exists(numbers: list[int], target_sum: int, expected: bool):
    assert sum_of_two_exists(numbers, target_sum) == expected
