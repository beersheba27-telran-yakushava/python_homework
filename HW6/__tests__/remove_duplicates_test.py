import pytest
from HW6.src.remove_duplicates import remove_duplicates

@pytest.mark.parametrize("numbers, expected", [
    ([-1, 0, 100, -1, 20, 80, 20], [-1, 0, 100, 20, 80]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([7, 7, 7, 7, 7], [7]),
    ([1, 2, 1, 2, 1, 2], [1, 2]),
    ([], []),
    ([42], [42]),
    ([0, -5, 0, 1000, -5], [0, -5, 1000])
])
def test_remove_duplicates(numbers: list[int], expected: list[int]):
    assert remove_duplicates(numbers) == expected
