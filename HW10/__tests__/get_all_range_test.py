import pytest
from collections.abc import Sequence
from HW10.src.get_all_range import get_all_range

@pytest.mark.parametrize(
    "numbers, allowed, expected",
    [
        ([1, 2, 3, 4, 5, 6, 7], range(2, 5), [2, 3, 4]),
        ([10, 20, 30, 40, 50], range(15, 45), [20, 30, 40]),
        ([1, 2, 2, 3, 4, 4, 4, 5], range(2, 4), [2, 2, 3]),
        ([5, 5, 5, 5], range(5, 6), [5, 5, 5, 5]),
        ([5, 5, 5, 5], range(5, 5), []),
        ([1, 2, 3], range(0, 10), [1, 2, 3]),
        ([1, 2, 3], range(1, 4), [1, 2, 3]),
        ([10, 20, 30], range(1, 10), []),
        ([10, 20, 30], range(31, 50), []),
        ([-10, -5, 0, 5, 10], range(-6, 5), [-5, 0]),
        ([1, 2, 3, 4], range(5, 5), []),
        ([1, 2, 3, 4], range(10, 2), []),
        ([], range(1, 10), []),
        ([], None, []),
    ],
)

def test_get_all_range_cases(numbers: Sequence[int], expected: list[int], allowed: range|None):
    assert get_all_range(numbers, allowed) == expected

def test_get_all_range_none_allowed():
    numbers = [1, 2, 3, 4, 5]
    result = get_all_range(numbers)

    assert result == [1, 2, 3, 4, 5]
    assert result is not numbers

def test_get_all_range_sequence_types():
    numbers_tuple = (10, 20, 30, 40)

    res_range = get_all_range(numbers_tuple, range(20, 40))
    assert res_range == [20, 30]
    assert isinstance(res_range, list)

    res_none = get_all_range(numbers_tuple)
    assert res_none == [10, 20, 30, 40]
    assert isinstance(res_none, list)
