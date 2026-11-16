import pytest
from HW8.src.merge import merge

def test_merge_default_numbers():
    part1 = [-11, 3, 5, 7]
    part2 = [-20, -10, 0, 4]
    assert merge(part1, part2) == [-20, -11, -10, 0, 3, 4, 5, 7]

def test_merge_with_abs_key():
    part1 = [3, 5, 7, -11]
    part2 = [0, 4, -10, -20]
    assert merge(part1, part2, key=lambda x: abs(x)) == [0, 3, 4, 5, 7, -10, -11, -20]

def test_merge_sequences_tuples_and_strings():
    part1 = (1, 4, 7)
    part2 = (2, 3, 8)
    res = merge(part1, part2)
    assert res == [1, 2, 3, 4, 7, 8]
    assert isinstance(res, list)

    assert merge("ace", "bdf") == ["a", "b", "c", "d", "e", "f"]

def test_merge_strings_by_length_and_case_insensitive():
    part1 = ["a", "ccc", "eeeee"]
    part2 = ["bb", "dddd"]
    assert merge(part1, part2, key=lambda s: len(s)) == ["a", "bb", "ccc", "dddd", "eeeee"]

    assert merge(
        ["Apple", "cherry"],
        ["banana", "Date"],
        key=lambda s: str(s).lower(),
    ) == ["Apple", "banana", "cherry", "Date"]


def test_merge_with_tuple_key():
    part1 = ["b", "aa", "ccc"]
    part2 = ["a", "bb"]
    result = merge(part1, part2, key=lambda s: (len(str(s)), str(s)))
    assert result == ["a", "b", "aa", "bb", "ccc"]

def test_merge_stability():
    part1 = ["a1", "b1"]
    part2 = ["a2", "b2"]
    assert merge(part1, part2, key=lambda s: str(s)[0]) == ["a1", "a2", "b1", "b2"]


def test_merge_custom_objects():
    users1: list[dict[str, int | str]] = [{"name": "Alice", "age": 20}, {"name": "Bob", "age": 35}]
    users2: list[dict[str, int | str]] = [{"name": "Charlie", "age": 25}, {"name": "Dave", "age": 35}]

    res = merge(users1, users2, key=lambda u: u["age"])
    assert res == [
        {"name": "Alice", "age": 20},
        {"name": "Charlie", "age": 25},
        {"name": "Bob", "age": 35},
        {"name": "Dave", "age": 35},
    ]

@pytest.mark.parametrize(
    "part1, part2, expected",
    [
        ([], [], []),
        ((), (), []),
        ([1, 2, 3], [], [1, 2, 3]),
        ([], (4, 5, 6), [4, 5, 6]),
        ([5], [2], [2, 5]),
        ([1, 2], [3, 4], [1, 2, 3, 4]),
    ],
)
def test_merge_edge_cases(
    part1: tuple[()] | list[int],
    part2: tuple[()] | list[int],
    expected: tuple[()] | list[int]
):
    assert merge(part1, part2) == expected

def test_merge_immutability():
    part1 = [1, 3, 5]
    part2 = [2, 4, 6]
    res = merge(part1, part2)

    assert res == [1, 2, 3, 4, 5, 6]
    assert res is not part1
    assert res is not part2
    assert part1 == [1, 3, 5]
    assert part2 == [2, 4, 6]
