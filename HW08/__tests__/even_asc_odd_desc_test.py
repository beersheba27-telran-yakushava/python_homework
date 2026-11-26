import pytest
from HW08.src.even_asc_odd_desc import even_asc_odd_desc

@pytest.mark.parametrize(
    "numbers, expected",
    [
        ([], []),
        ([4], [4]),
        ([-5], [-5]),
        ([0, -2, 2, -1, 1], [-2, 0, 2, 1, -1]),
        ([8, -4, 0, 2, -10], [-10, -4, 0, 2, 8]),
        ([-5, 7, 1, -9, 3], [7, 3, 1, -5, -9]),
        ([-4, 2, 6, 9, 3, -1], [-4, 2, 6, 9, 3, -1]),
        ([-3, 1, 5, 4, 2, -6], [-6, 2, 4, 5, 1, -3]),
        ([3, 2, 3, 2, -1, -2, -1, -2], [-2, -2, 2, 2, 3, 3, -1, -1]),
    ],
)
def test_even_asc_odd_desc_cases(
    numbers: list[int], expected: list[int]
) -> None:
    assert even_asc_odd_desc(numbers) == expected


def test_returns_new_list_without_mutating_original() -> None:
    original: list[int] = [3, 4, 1, 2]
    result: list[int] = even_asc_odd_desc(original)

    assert original == [3, 4, 1, 2]
    assert result is not original
    assert isinstance(result, list)
    assert result == [2, 4, 3, 1]
