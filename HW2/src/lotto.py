import random

def distinct_random_numbers(min: int, max: int, size: int) -> list[int]:
    """
    returns list with "size" distinct random numbers 
    each number >= "min" and <= "max"
    if creating "size" distinct random numbers is impossible, return empty array
    """
    is_valid_condition: bool = size > 0 and max - min + 1 >= size

    return random.sample(range(min, max+1), size) if is_valid_condition else []
