import pytest
from HW4.src.intersection import intersection

@pytest.mark.parametrize("l1, l2, expected", [
    ([1, 2, 3], [4, 3, 1], [1, 3]),
    ([1, 2, 3], [4, 5, 6], []),
    ([], [1, 2, 3], []),
    ([1, 2, 3], [], []),
    ([], [], []),
    ([1, 2, 3], [1, 2, 3], [1, 2, 3]),
    ([-5, 0, 5, 10], [5, -5, 99], [-5, 5])
])

def test_intersection(l1: list[int], l2: list[int], expected: list[int]):
    assert sorted(intersection(l1, l2)) == sorted(expected)
