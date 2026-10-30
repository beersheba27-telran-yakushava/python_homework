def last_index_of(numbers: list[int], num: int):
    """
    "numbers" - list with int numbers; "num" - int
    if "num" exists in "numbers", returns index of its last occurrence,
    otherwise -1. Examples: lastIndexOf([10, 20, 30, 20, -1],20) => 3,
    lastIndexOf([10, 20, 30, 20, -1],23) => -1
    """
    index = len(numbers) - 1
    while index >= 0:
        if numbers[index] == num:
            return index
        index -= 1
    return -1
