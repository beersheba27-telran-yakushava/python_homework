import pytest
from HW6.src.bubble_sort import bubble_sort

@pytest.mark.parametrize("arr, expected", [
    ([100, 90, 80, 70], [70, 80, 90, 100]),
    ([70, 80, 90, 100], [70, 80, 90, 100]),
    ([], []),
    ([42], [42]),
    ([5, 1, 5, 3, 1], [1, 1, 3, 5, 5]),
    ([-5, 0, -10, 5, 2], [-10, -5, 0, 2, 5]),
    ([1000, -1000, 0], [-1000, 0, 1000])
])

def test_bubble_sort(arr: list[int], expected: list[int]):
    assert bubble_sort(arr) == expected
