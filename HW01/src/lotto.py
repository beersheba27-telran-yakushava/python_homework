import random

def exists(numbers: list[int], num: int) -> bool:
    """
    returns True if "num" exists in list "numbers" otherwise False
    """
    return num in numbers

def distinct_random_numbers(min: int, max: int, size: int) -> list[int]:
    """
    returns list with "size" distinct random numbers 
    each number >= "min" and <= "max"
    if creating "size" distinct random numbers is impossible, return empty array
    requirement: to use the above function "exists" and one while-loop
    """
    numbers: list[int] = []
    valid_condition: bool = size > 0 and max - min + 1 >= size

    while valid_condition and len(numbers) < size:
        num = random.randint(min, max)
        if not exists(numbers, num): numbers.append(num)

    return numbers
