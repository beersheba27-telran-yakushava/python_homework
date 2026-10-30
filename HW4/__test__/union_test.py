import pytest
from HW4.src.union import union

@pytest.mark.parametrize("l1, l2, expected", [
    ([1, 2, 3], [4, 3, 1], [1, 2, 3, 4]),
    ([1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6]),
    ([], [4, 5, 6], [4, 5, 6]),
    ([1, 2, 3], [], [1, 2, 3]),
    ([], [], []),
    ([1, 2, 3], [1, 2, 3], [1, 2, 3]),
    ([-5, 0], [0, 5, -5], [-5, 0, 5])
])

def test_union(l1: list[int], l2: list[int], expected: list[int]):
    assert sorted(union(l1, l2)) == sorted(expected)
