import pytest
from HW12.src.min_max_avg import min_max_avg

@pytest.mark.parametrize(
    ("numbers", "expected"),
    [
        ([], {}),
        ([7], {"min": 7, "max": 7, "avg": 7}),
        ([-4, 2, 8], {"min": -4, "max": 8, "avg": 2}),
        ([1, 2, 4], {"min": 1, "max": 4, "avg": 2}),
        ([1, 2, 5], {"min": 1, "max": 5, "avg": 3}),
        ([1, 4], {"min": 1, "max": 4, "avg": 2}),
        ([2, 5], {"min": 2, "max": 5, "avg": 4}),
    ],
)

def test_min_max_avg_cases(
    numbers: list[int],
    expected: dict[str, int],
) -> None:
    assert min_max_avg(numbers) == expected
