import pytest
from HW12.src.get_occurrences_counts import get_occurrences_counts

@pytest.mark.parametrize(
    ("strings", "expected"),
    [
        ([], []),
        (["x", "x", "x"], ["x=>3"]),
        (
            ["b", "a", "b", "c", "b", "a"],
            ["b=>3", "a=>2", "c=>1"],
        ),
        (["z", "a", "b"], ["a=>1", "b=>1", "z=>1"]),
    ],
)

def test_get_occurrences_counts_cases(
    strings: list[str],
    expected: list[str],
) -> None:
    assert get_occurrences_counts(strings) == expected
