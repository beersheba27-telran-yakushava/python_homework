import pytest
from collections.abc import Sequence
from typing import Any

from HW08.src.bubble_sorted import bubble_sorted

def test_standard_numbers_sort() -> None:
    numbers: list[int] = [5, -11, 3, 0, -20, 7]
    assert bubble_sorted(numbers) == [-20, -11, 0, 3, 5, 7]

def test_standard_strings_sort() -> None:
    words: list[str] = ["Vasya", "aaa", "BBB", "bb"]
    assert bubble_sorted(words) == ["BBB", "Vasya", "aaa", "bb"]

def test_sort_with_abs_positional() -> None:
    numbers: list[int] = [3, -11, 5, 0, -20, 4]
    assert bubble_sorted(numbers, abs) == [0, 3, 4, 5, -11, -20]

def test_sort_with_abs_keyword() -> None:
    numbers: list[int] = [3, -11, 5, 0, -20, 4]
    assert bubble_sorted(numbers, key=abs) == [0, 3, 4, 5, -11, -20]

def test_sort_strings_by_length() -> None:
    words: list[str] = ["Vasya", "aaa", "BB", "b"]
    assert bubble_sorted(words, len) == ["b", "BB", "aaa", "Vasya"]

def test_sort_strings_case_insensitive() -> None:
    words: list[str] = ["Vasya", "aaa", "BBB", "bb"]
    assert bubble_sorted(words, lambda s: str(s).lower()) == [
        "aaa",
        "bb",
        "BBB",
        "Vasya",
    ]

def test_sort_by_multiple_criteria_tuples() -> None:
    numbers: list[int] = [5, 2, 9, 8, 1, 4]
    result = bubble_sorted(numbers, lambda n: (int(n) % 2, n))
    assert result == [2, 4, 8, 1, 5, 9]

def test_sort_custom_objects() -> None:
    people: list[dict[str, Any]] = [
        {"name": "Bob", "age": 30},
        {"name": "Alice", "age": 25},
        {"name": "Charlie", "age": 25},
    ]
    sorted_people = bubble_sorted(people, lambda p: (p["age"], p["name"]))
    assert sorted_people == [
        {"name": "Alice", "age": 25},
        {"name": "Charlie", "age": 25},
        {"name": "Bob", "age": 30},
    ]

@pytest.mark.parametrize(
    "input_seq, expected",
    [
        ([], []),
        ((), []),
        ([42], [42]),
        ([1, 2, 3, 4], [1, 2, 3, 4]),
        ([4, 3, 2, 1], [1, 2, 3, 4]),
        ([5, 5, 5, 5], [5, 5, 5, 5]),
    ],
)
def test_edge_cases(input_seq: Sequence[int], expected: list[int]) -> None:
    assert bubble_sorted(input_seq) == expected

def test_immutability_and_return_type() -> None:
    original_list: list[int] = [3, 1, 2]
    original_tuple: tuple[int, ...] = (3, 1, 2)

    res_from_list = bubble_sorted(original_list)
    res_from_tuple = bubble_sorted(original_tuple)

    assert original_list == [3, 1, 2]
    assert res_from_list is not original_list

    assert isinstance(res_from_tuple, list)
    assert res_from_tuple == [1, 2, 3]

def test_sort_stability() -> None:
    words: list[str] = ["cat", "elephant", "dog", "ant", "bat"]
    assert bubble_sorted(words, len) == ["cat", "dog", "ant", "bat", "elephant"]
