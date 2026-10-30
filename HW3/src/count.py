def count(numbers: list[int], num: int) -> int:
    """
    "numbers" - list with int numbers; "num" - int
    returns count of "num" occurrences in "numbers".
    Examples: count([10, 20, 30, 20, -1],20) => 2,
    count([10, 20, 30, 20, -1],23) => 0
    """
    counter = 0
    index = 0
    while index < len(numbers):
        if numbers[index] == num:
            counter += 1
        index += 1
    return counter
