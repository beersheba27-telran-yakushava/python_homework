import pytest
from HW3.src.last_index_of import last_index_of

@pytest.mark.parametrize(
    "numbers, num, expected",
    [
        ([10, 20, 30, 20, -1], 20, 3),
        ([10, 20, 30, 20, -1], 23, -1),
        ([5, 5, 5, 5], 5, 3),
        ([], 10, -1),
        ([3, 1, 2], 3, 0),
        ([1, 2, 3], 3, 2),
    ]
)
def test_last_index_of(numbers: list[int], num: int, expected: int):
    assert last_index_of(numbers, num) == expected
