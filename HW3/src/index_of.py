def index_of(numbers: list[int], num: int):
    """
    "numbers" - list with int numbers; "num" - int
    if "num" exists in "numbers", returns index of its first occurrence,
    otherwise -1. Examples: indexOf([10, 20, 30, 20, -1],20) => 1,
    indexOf([10, 20, 30, 20, -1],23) => -1
    """
    index = 0

    while index < len(numbers) and numbers[index] != num:
        index += 1

    return index if index < len(numbers) else -1
