def index_of(numbers: list[int], num: int):
    """
    "numbers" - list with int numbers; "num" - int
    if "num" exists in "numbers", returns index of its first occurrence,
    otherwise -1. Examples: indexOf([10, 20, 30, 20, -1],20) => 1,
    indexOf([10, 20, 30, 20, -1],23) => -1
    """
    index = 0
    while index < len(numbers):
        if numbers[index] == num:
            return index
        index += 1
    return -1
