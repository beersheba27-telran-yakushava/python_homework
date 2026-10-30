import pytest
from HW4.src.difference import difference

@pytest.mark.parametrize("l1, l2, expected", [
    ([1, 2, 3], [4, 3, 1], [2]),
    ([1, 2, 3], [4, 5, 6], [1, 2, 3]),
    ([], [1, 2, 3], []),
    ([1, 2, 3], [], [1, 2, 3]),
    ([], [], []),
    ([1, 2, 3], [1, 2, 3], []),
    ([-5, 0, 5, 10], [5, -5, 99], [0, 10])
])

def test_difference(l1: list[int], l2: list[int], expected: list[int]):
    assert sorted(difference(l1, l2)) == sorted(expected)
