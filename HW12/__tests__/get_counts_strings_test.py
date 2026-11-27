import pytest
from HW12.src.get_counts_strings import get_counts_strings

@pytest.mark.parametrize(
    ("strings", "expected"),
    [
        ([], {}),
        (["x", "x", "x"], {3: ["x"]}),
        (
            ["b", "a", "b", "a", "b", "c"],
            {3: ["b"], 2: ["a"], 1: ["c"]},
        ),
        (["z", "a", "b"], {1: ["a", "b", "z"]}),
    ],
)

def test_get_counts_strings_cases(
    strings: list[str],
    expected: dict[int, list[str]],
) -> None:
    assert get_counts_strings(strings) == expected
