import pytest
from HW7.src.binary_search import binary_search

@pytest.fixture
def sample_numbers() -> list[int]:
    return [10, 10, 10, 20, 20, 20, 30, 30, 40]


@pytest.mark.parametrize(
    "num, expected",
    [
        (10, 0),
        (20, 3),
        (30, 6),
        (40, 8),
        (5, -1),
        (15, -4),
        (25, -7),
        (35, -9),
        (45, -10),
    ],
)
def test_binary_search_with_duplicates(sample_numbers: list[int], num: int, expected: int):
    assert binary_search(sample_numbers, num) == expected


@pytest.mark.parametrize(
    "numbers, num, expected",
    [
        ([], 10, -1),
        ([10], 10, 0),
        ([10], 5, -1),
        ([10], 15, -2),
        ([10, 10, 10], 10, 0),
        ([10, 10, 10], 5, -1),
        ([10, 10, 10], 15, -4),
        ([-30, -20, -10], -20, 1),
        ([-30, -20, -10], -25, -2),
    ],
)
def test_binary_search_edge_cases(numbers: list[int], num: int, expected: int):
    assert binary_search(numbers, num) == expected
