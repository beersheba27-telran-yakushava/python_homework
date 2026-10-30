import pytest
from HW1.src.lotto import distinct_random_numbers

@pytest.mark.parametrize("min_val, max_val, size, expected_len", [
    (10, 50, 5, 5),
    (1, 5, 5, 5),
    (1, 5, 10, 0),
    (20, 10, 5, 0),
    (1, 10, 0, 0),
    (1, 10, -3, 0),
    (-5, 0, 4, 4)
])

def test_unique_random_list(min_val: int, max_val: int, size: int, expected_len: int):
    result = distinct_random_numbers(min_val, max_val, size)

    assert len(result) == expected_len
    assert len(set(result)) == len(result)
    assert all(min_val <= x <= max_val for x in result)
