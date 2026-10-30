import pytest
from HW3.src.index_of import index_of

@pytest.mark.parametrize(
    "numbers, num, expected",
    [
        ([10, 20, 30, 20, -1], 20, 1),
        ([10, 20, 30, 20, -1], 23, -1),
        ([5, 5, 5, 5], 5, 0),
        ([], 10, -1),
        ([1, 2, 3], 3, 2),
        ([1, 2, 3], 1, 0),
    ]
)
def test_index_of(numbers: list[int], num: int, expected: int):
    assert index_of(numbers, num) == expected
