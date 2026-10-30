import pytest
from HW2.src.palindromic_numbers import create_palindromic_list

@pytest.mark.parametrize("start, stop, expected", [
    (1, 9, [1, 2, 3, 4, 5, 6, 7, 8, 9]),
    (8, 12, [8, 9, 11]),
    (12, 8, [11, 9, 8]),
    (11, 22, [11, 22]),
    (95, 105, [99, 101]),
    (105, 95, [101, 99]),
    (5, 5, [5]),
    (12, 12, [])
])
def test_get_palindromic_numbers(start: int, stop: int, expected: list[int]):
    assert create_palindromic_list(start, stop) == expected
