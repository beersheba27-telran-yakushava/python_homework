import pytest
from HW3.src.count import count

@pytest.mark.parametrize(
    "numbers, num, expected",
    [
        ([10, 20, 30, 20, -1], 20, 2),
        ([10, 20, 30, 20, -1], 23, 0),
        ([], 10, 0),
        ([5, 5, 5, 5, 5], 5, 5),
        ([1, 2, 3, 4, 1], 1, 2),
    ]
)
def test_count(numbers: list[int], num: int, expected: int):
    assert count(numbers, num) == expected
