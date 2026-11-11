import pytest
from HW7.src.insert_sorted import insert_sorted

@pytest.fixture
def initial_numbers() -> list[int]:
    return [10, 10, 10, 20, 20, 20, 30, 30, 40]


@pytest.mark.parametrize(
    "num, expected",
    [
        (19, [10, 10, 10, 19, 20, 20, 20, 30, 30, 40]),
        (20, [10, 10, 10, 20, 20, 20, 20, 30, 30, 40]),
        (5, [5, 10, 10, 10, 20, 20, 20, 30, 30, 40]),
        (10, [10, 10, 10, 10, 20, 20, 20, 30, 30, 40]),
        (25, [10, 10, 10, 20, 20, 20, 25, 30, 30, 40]),
        (40, [10, 10, 10, 20, 20, 20, 30, 30, 40, 40]),
        (45, [10, 10, 10, 20, 20, 20, 30, 30, 40, 45]),
    ],
)
def test_insert_sorted_basic(initial_numbers: list[int], num: int, expected: list[int]):
    original_ref = initial_numbers

    result = insert_sorted(initial_numbers, num)

    assert result is None
    assert initial_numbers == expected
    assert initial_numbers is original_ref


@pytest.mark.parametrize(
    "numbers, num, expected",
    [
        ([], 10, [10]),
        ([10], 5, [5, 10]),
        ([10], 15, [10, 15]),
        ([10], 10, [10, 10]),
        ([-30, -10], -20, [-30, -20, -10]),
    ],
)
def test_insert_sorted_edge_cases(numbers: list[int], num: int, expected: list[int]):
    result = insert_sorted(numbers, num)

    assert result is None
    assert numbers == expected
