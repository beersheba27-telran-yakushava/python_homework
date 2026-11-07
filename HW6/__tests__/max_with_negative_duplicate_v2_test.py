import pytest
from HW6.src.max_with_negative_duplicate import max_with_negative_duplicate

@pytest.mark.parametrize("numbers, expected", [
    ([-100, 20, 10, -10, 1, 1, 5, -30, -20, 100], 100),
    ([10, 20, -15, -11, 20], -1),
    ([10, -10, 5, -5, 20, -20], 20),
    ([0, 5, 10, -5], 5),
    ([0, 1, 2, 3], -1),
    ([], -1),
    ([100], -1),
    ([-100], -1),
    ([-1, -2, -3, -4], -1),
    ([1, 2, 3, 4], -1),
    ([10, 10, 10, -5], -1),
    ([1000000, -1000000, 5], 1000000)
])
def test_max_with_negative_duplicate(numbers: list[int], expected: int):
    assert max_with_negative_duplicate(numbers) == expected
