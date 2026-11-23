from collections.abc import Sequence
from dataclasses import dataclass
import random
import pytest

from HW10.src.my_sorted import my_sorted

@dataclass(frozen=True)
class Person:
    name: str
    age: int

@pytest.mark.parametrize(
    "items, expected",
    [
        ([], []),
        ([42], [42]),
        ([4, 2, 3, 1], [1, 2, 3, 4]),
        ([9, 3, 7, 1, 8, 2, 6, 4, 5], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
        ([10, 5], [5, 10]),
        ([3, 1, 2], [1, 2, 3]),
        ([50, 10, 40, 20, 30], [10, 20, 30, 40, 50]),
        ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([3, 1, 2, 3, 1, 2], [1, 1, 2, 2, 3, 3]),
        ([-5, 10, -10, 0, 5], [-10, -5, 0, 5, 10]),
    ],
)
def test_my_sorted_numbers(items: list[int], expected: list[int]) -> None:
    assert my_sorted(items) == expected

def test_my_sorted_with_key_len() -> None:
    words: list[str] = ["banana", "pie", "apple", "a", "kiwi", "hi"]
    result: list[str] = my_sorted(words, key=len)
    assert result == ["a", "hi", "pie", "kiwi", "apple", "banana"]

def test_my_sorted_stability_with_objects() -> None:
    people: list[Person] = [
        Person("Alice", 30),
        Person("Bob", 25),
        Person("Charlie", 30),
        Person("David", 25),
        Person("Eve", 20),
    ]
    result: list[Person] = my_sorted(people, key=lambda p: p.age)
    assert result == [
        Person("Eve", 20),
        Person("Bob", 25),
        Person("David", 25),
        Person("Alice", 30),
        Person("Charlie", 30),
    ]

def test_my_sorted_sequence_and_immutability() -> None:
    original_list: list[int] = [5, 2, 8, 1, 9]
    sorted_from_list: list[int] = my_sorted(original_list)
    assert sorted_from_list == [1, 2, 5, 8, 9]
    assert original_list == [5, 2, 8, 1, 9]

    original_tuple: Sequence[int] = (40, 10, 30, 20)
    sorted_from_tuple: list[int] = my_sorted(original_tuple)
    assert sorted_from_tuple == [10, 20, 30, 40]
    assert isinstance(sorted_from_tuple, list)

def test_my_sorted_large_random() -> None:
    rng = random.Random(42)
    data: list[int] = [rng.randint(-1000, 1000) for _ in range(100)]
    assert my_sorted(data) == sorted(data)
