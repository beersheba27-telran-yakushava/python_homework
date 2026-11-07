import pytest
from HW6.src.bubble_sort import bubble_sort

@pytest.mark.parametrize("arr, expected", [
    ([100, 90, 80, 70], [70, 80, 90, 100]),
    ([1, 2, 3, 4], [1, 2, 3, 4]),
    ([], []),
    ([42], [42]),
    ([5, 1, 5, 2, 1], [1, 1, 2, 5, 5]),
    ([-5, 0, -10, 5, 2], [-10, -5, 0, 2, 5])
])
def test_bubble_sort_inplace(arr: list[int], expected: list[int]):
    test_list = arr.copy()
    
    result = bubble_sort(test_list)
    assert result is None
    assert test_list == expected
