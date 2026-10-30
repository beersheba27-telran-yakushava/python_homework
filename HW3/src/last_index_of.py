def last_index_of(numbers: list[int], num: int) -> int:
    """
    "numbers" - list with int numbers; "num" - int
    if "num" exists in "numbers", returns index of its last occurrence,
    otherwise -1. Examples: lastIndexOf([10, 20, 30, 20, -1],20) => 3,
    lastIndexOf([10, 20, 30, 20, -1],23) => -1
    """
    index = len(numbers) - 1

    while index >= 0 and numbers[index] != num:
        index -= 1

    return index if index >= 0 else -1
