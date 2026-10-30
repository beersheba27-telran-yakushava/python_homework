import pytest
from symmetric_difference import symmetric_difference

@pytest.mark.parametrize("l1, l2, expected", [
    ([1, 2, 3], [4, 3, 1], [2, 4]),
    ([1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6]),
    ([], [4, 5, 6], [4, 5, 6]),
    ([1, 2, 3], [], [1, 2, 3]),
    ([], [], []),
    ([1, 2, 3], [1, 2, 3], []),
    ([-5, 0], [0, 5], [-5, 5])
])

def test_symmetric_difference(l1: list[int], l2: list[int], expected: list[int]):
    assert sorted(symmetric_difference(l1, l2)) == sorted(expected)
