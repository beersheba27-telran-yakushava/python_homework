import pytest
from HW5.src.move_max_to_end import move_max_to_end

@pytest.mark.parametrize("initial_list, expected_list", [
    ([100, 20, 30, 40, 50], [20, 30, 40, 50, 100]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([1, 2, 10, 3, 4], [1, 2, 3, 4, 10]),
    ([-5, -1, -3, -4], [-5, -3, -4, -1]),
    ([42], [42]),
    ([10, 2, 10, 3], [2, 10, 3, 10])
])

def test_move_max_to_end(initial_list: list[int], expected_list: list[int]):
    l1 = initial_list.copy()
    
    result = move_max_to_end(l1)
    assert result is None

    assert l1 == expected_list

def test_move_max_to_end_empty_list():
    empty_list: list[int] = []

    with pytest.raises(ValueError) as exc_info:
        move_max_to_end(empty_list)

    assert str(exc_info.value) == "Сonnot process an empty list"
