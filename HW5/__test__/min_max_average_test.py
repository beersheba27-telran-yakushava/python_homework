import pytest
from HW5.src.min_max_average import min_max_average

@pytest.mark.parametrize("numbers, expected", [
    ([1, 2, 3, 4, 5], (1, 5, 3.0)),
    ([-5, 0, 5, 10], (-5, 10, 2.5)),
    ([7, 7, 7], (7, 7, 7.0)),
    ([42], (42, 42, 42.0)),
    ([3, 5, 8], (3, 8, 5.333333333333333)),
    ([1000, 2000, 3000], (1000, 3000, 2000.0))
])

def test_min_max_average(numbers: list[int], expected: tuple[int, int, float]):
    res_min, res_max, res_avg = min_max_average(numbers)

    assert isinstance(res_min, int)
    assert isinstance(res_max, int)
    assert isinstance(res_avg, float)

    exp_min, exp_max, exp_avg = expected
    assert res_min == exp_min
    assert res_max == exp_max
    assert res_avg == pytest.approx(exp_avg)

def test_min_max_average_empty_list():
    empty_list: list[int] = []

    with pytest.raises(ValueError) as exc_info:
       min_max_average(empty_list)

    assert str(exc_info.value) == "Сonnot process an empty list"
