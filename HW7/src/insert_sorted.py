from HW7.src.binary_search import binary_search

def insert_sorted(numbers: list[int], num: int) -> None:
    """
    numbers: sorted list
    num: inserted number
    inserts "num" keeping "numbers" sorted
    For example: numbers: list[int] = [10, 10, 10, 20, 20, 20, 30, 30, 40]
    after insert_sorted (numbers, 19) the list will contain [10, 10, 10, 19, 20, 20, 20, 30, 30, 40]
    after insert_sorted (numbers, 20) (initial list) the list will contain [10, 10, 10, 20, 20, 20, 20, 30, 30, 40]
    """
    index: int = binary_search(numbers, num)
    if index < 0:
        index = -index - 1
    numbers[index:index] = [num]
