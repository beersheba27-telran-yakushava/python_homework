import pytest
from HW3.src.sum_of_two_exists import sum_of_two_exists

@pytest.mark.parametrize(
    "numbers, sum, expected",
    [
        ([1, -1, 40, 50, 0], 0, True),
        ([1, -1, 40, 50, 0], 42, False),
        ([10, 20, 30], 40, True),
        ([5, 10, 15], 10, False),
        ([5, 5, 15], 10, True),
        ([1, 2], 3, True),
        ([1], 1, False),
        ([], 0, False),
    ]
)
def test_sum_of_two_exists(numbers: list[int], sum: int, expected: bool):
    assert sum_of_two_exists(numbers, sum) == expected
