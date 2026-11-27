from functools import reduce

def min_max_avg(numbers: list[int]) -> dict[str, int]:
    """
    returns dictionary with minimal, maximal and rounded to int avg values
    that is dictionary with three pairs if list isn't empty and with no pairs otherwise
    additional requirement: to use function "reduce" (from functools import reduce)
    """
    if not numbers: return {}

    minimum, maximum, total = reduce(
        _accumulate,
        numbers,
        (numbers[0], numbers[0], 0),
    )

    return {
        "min": minimum,
        "max": maximum,
        "avg": round(total / len(numbers)),
    }

def _accumulate(
    values: tuple[int, int, int],
    number: int,
) -> tuple[int, int, int]:
    minimum, maximum, total = values
    return min(minimum, number), max(maximum, number), total + number
