import pytest
from collections.abc import Sequence
from HW10.src.get_all_not_in_range import get_all_not_in_range

@pytest.mark.parametrize(
    "numbers, disallowed, expected",
    [
        ([1, 2, 3, 4, 5, 6], range(2, 5), [1, 5, 6]),
        ([10, 20, 30, 40, 50], range(20, 40), [10, 40, 50]),
        ([1, 2, 2, 3, 4, 4, 5], range(2, 4), [1, 4, 4, 5]),
        ([5, 5, 5, 6, 7], range(5, 6), [6, 7]),
        ([15, 20, 25, 30], range(1, 10), [15, 20, 25, 30]),
        ([15, 20, 25, 30], range(31, 50), [15, 20, 25, 30]),
        ([1, 2, 3], range(0, 10), []),
        ([1, 2, 3], range(1, 4), []),
        ([-10, -5, 0, 5, 10], range(-5, 6), [-10, 10]),
        ([1, 2, 3], range(5, 5), [1, 2, 3]),
        ([1, 2, 3], range(10, 2), [1, 2, 3]),
        ([], range(1, 10), []),
        ([], range(5, 5), []),
    ],
)

def test_get_all_not_in_range_cases(
    numbers: Sequence[int],
    disallowed: range,
    expected: list[int],
) -> None:
    assert get_all_not_in_range(numbers, disallowed) == expected

def test_get_all_not_in_range_returns_new_list() -> None:
    numbers: list[int] = [1, 2, 3]
    result: list[int] = get_all_not_in_range(numbers, range(5, 5))

    assert result == [1, 2, 3]
    assert result is not numbers

def test_get_all_not_in_range_sequence_types() -> None:
    numbers_tuple: tuple[int, ...] = (10, 20, 30, 40, 50)
    result: list[int] = get_all_not_in_range(numbers_tuple, range(20, 40))

    assert result == [10, 40, 50]
    assert isinstance(result, list)
