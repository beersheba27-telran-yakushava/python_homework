import pytest
from HW3.src.min_even import min_even

@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([-10001, 10, 20, 8, -7], 8),
        ([2, 4, 6, 8], 2),
        ([-2, -4, -6, -8], -8),
        ([1, 3, 5, 0, 7], 0),
        ([42], 42),
        ([10, -20, 30, -20], -20),
    ]
)
def test_min_even(numbers: list[int], expected: int):
    assert min_even(numbers) == expected
