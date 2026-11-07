def sum_of_two_exists(numbers:list[int], sum: int) -> bool:
    """
    Algorithm complexity should be O[N]
    "numbers" - list with int numbers; "sum" - int
    returns True if "numbers" includes two numbers, sum of which equals "sum"
    Examples: sumOfTwoExists([1, -1, 40, 50, 0], 0) => True;
    sumOfTwoExists([1, -1, 40, 50, 0], 42) => False
    """
    seen: set[int] = set()

    for num in numbers:
        complement = sum - num
        if complement in seen:
            return True
        seen.add(num)

    return False
