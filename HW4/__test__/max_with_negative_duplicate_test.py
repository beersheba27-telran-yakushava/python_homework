import pytest
from HW4.src.max_with_negative_duplicate import max_with_negative_duplicate

@pytest.mark.parametrize("numbers, expected", [
    ([-100, 20, 10, -10, 1, 1, 5, -30, -20, 100], 100),
    ([10, 20, -15, -11, 20], -1),
    ([50, -20, 20, -5, -2], 20),
    ([-5, 5], 5),
    ([0, 10, 20, -30], -1),
    ([1, 2, 3, 4, 5], -1),
    ([-1, -2, -3, -4], -1),
    ([], -1)
])

def test_max_with_negative_duplicate(numbers: list[int], expected: int):
    assert max_with_negative_duplicate(numbers) == expected
