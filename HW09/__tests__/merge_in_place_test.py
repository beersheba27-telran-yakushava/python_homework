import pytest
from HW09.src.merge_in_place import merge_in_place

def test_merge_default_numbers():
    items = [-11, 3, 5, 7, -20, -10, 0, 4]
    res = merge_in_place(items, start=0, len1=4, size=8)
    assert res is None
    assert items == [-20, -11, -10, 0, 3, 4, 5, 7]


def test_merge_with_abs_key():
    items = [3, 5, 7, -11, 0, 4, -10, -20, 100, -80, -4, 8]
    merge_in_place(items, start=0, len1=4, size=8, key=abs)
    assert items == [0, 3, 4, 5, 7, -10, -11, -20, 100, -80, -4, 8]


def test_merge_middle_subpart():
    items = [999, 888, 1, 4, 7, 2, 3, 8, -777]
    merge_in_place(items, start=2, len1=3, size=6)
    assert items == [999, 888, 1, 2, 3, 4, 7, 8, -777]


def test_merge_strings_by_length_and_case_insensitive():
    items_len = ["a", "ccc", "eeeee", "bb", "dddd"]
    merge_in_place(items_len, start=0, len1=3, size=5, key=len)
    assert items_len == ["a", "bb", "ccc", "dddd", "eeeee"]

    items_case = ["Apple", "cherry", "banana", "Date"]
    merge_in_place(items_case, start=0, len1=2, size=4, key=str.lower)
    assert items_case == ["Apple", "banana", "cherry", "Date"]


def test_merge_with_tuple_key():
    items = ["b", "aa", "ccc", "a", "bb"]
    merge_in_place(items, start=0, len1=3, size=5, key=lambda s: (len(s), s))
    assert items == ["a", "b", "aa", "bb", "ccc"]


def test_merge_stability():
    items = ["a1", "b1", "a2", "b2"]
    merge_in_place(items, start=0, len1=2, size=4, key=lambda s: s[0])
    assert items == ["a1", "a2", "b1", "b2"]


def test_merge_custom_objects():
    items: list[dict[str, int | str]] = [
        {"name": "Alice", "age": 20},
        {"name": "Bob", "age": 35},
        {"name": "Charlie", "age": 25},
        {"name": "Dave", "age": 35},
    ]

    merge_in_place(items, start=0, len1=2, size=4, key=lambda u: int(u["age"]))
    assert items == [
        {"name": "Alice", "age": 20},
        {"name": "Charlie", "age": 25},
        {"name": "Bob", "age": 35},
        {"name": "Dave", "age": 35},
    ]


@pytest.mark.parametrize(
    "items, start, len1, size, expected",
    [
        ([], 0, 0, 0, []),
        ([1, 2, 3], 0, 3, 3, [1, 2, 3]),
        ([4, 5, 6], 0, 0, 3, [4, 5, 6]),
        ([5, 2], 0, 1, 2, [2, 5]),
        ([1, 2, 3, 4], 0, 2, 4, [1, 2, 3, 4]),
        ([3, 4, 1, 2], 0, 2, 4, [1, 2, 3, 4]),
    ],
)
def test_merge_edge_cases(
    items: list[int],
    start: int,
    len1: int,
    size: int,
    expected: list[int],
):
    merge_in_place(items, start=start, len1=len1, size=size)
    assert items == expected


def test_merge_in_place_memory_reference():
    items = [1, 3, 5, 2, 4, 6]
    original_ref = items

    res = merge_in_place(items, start=0, len1=3, size=6)

    assert res is None
    assert items == [1, 2, 3, 4, 5, 6]
    assert items is original_ref
