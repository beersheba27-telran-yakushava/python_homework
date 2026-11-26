import random
from collections.abc import Callable
from dataclasses import dataclass
from typing import Any
import pytest

from HW11.src.my_sorted import my_sorted

@dataclass(frozen=True)
class Person:
    name: str
    age: int

def test_empty_sequence():
    assert my_sorted([]) == []
    assert my_sorted(()) == []

def test_single_element():
    assert my_sorted([42]) == [42]
    assert my_sorted((42,)) == [42]

def test_already_sorted():
    data = [1, 2, 3, 4, 5]
    assert my_sorted(data) == [1, 2, 3, 4, 5]

def test_reverse_sorted():
    data = [5, 4, 3, 2, 1]
    assert my_sorted(data) == [1, 2, 3, 4, 5]

def test_duplicates_and_negatives():
    data = [3, -1, 0, 3, -5, -1, 2, 0]
    assert my_sorted(data) == sorted(data)

def test_input_sequence_not_mutated():
    original = [10, 3, 7, 1, 9, 2]
    copy_before = original.copy()
    result = my_sorted(original)

    assert original == copy_before  # Исходный список не изменился
    assert result is not original   # Возвращён новый список
    assert result == [1, 2, 3, 7, 9, 10]

def test_tuple_and_range_inputs():
    assert my_sorted((3, 1, 2)) == [1, 2, 3]
    assert my_sorted(range(5, 0, -1)) == [1, 2, 3, 4, 5]
    assert my_sorted(range(0)) == []

def test_signature_constraints():
    with pytest.raises(TypeError):
        my_sorted(items=[3, 1, 2])  # type: ignore

    with pytest.raises(TypeError):
        my_sorted([3, 1, 2], abs)  # type: ignore

@pytest.mark.parametrize(
    "data, key_func",
    [
        ([-10, 5, -2, 1, -20], abs),
        ([10, 2, 100, 5, 20], str),
        (["banana", "pie", "Washington", "book"], len),
        (["Banana", "apple", "Cherry"], str.lower),
    ],
)
def test_sort_with_key(data: list[Any], key_func: Callable[[Any], Any]):
    assert my_sorted(data, key=key_func) == sorted(data, key=key_func)

def test_stability_with_tuples_and_objects():
    people = [
        Person("Vasya", 20),
        Person("Abram", 60),
        Person("Kolya", 60),
        Person("Petya", 20),
    ]
    result = my_sorted(people, key=lambda p: p.age)
    assert result == sorted(people, key=lambda p: p.age)

def test_random_lists():
    rng = random.Random(42)
    for size in (2, 5, 10, 50, 200):
        data = [rng.randint(-500, 500) for _ in range(size)]
        assert my_sorted(data) == sorted(data)
        assert my_sorted(data, key=abs) == sorted(data, key=abs)
