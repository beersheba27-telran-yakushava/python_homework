def sum_of_two_exists(numbers: list[int], sum: int):
    """
    Optional task for advanced students
    To apply only the types discussed at the course up to now
    "numbers" - list with int numbers; "sum" - int
    returns True if "numbers" includes two numbers, sum of which equals "sum"
    Examples: sumOfTwoExists([1, -1, 40, 50, 0], 0) => True;
    sumOfTwoExists([1, -1, 40, 50, 0], 42) => False
    """
    i = 0
    length = len(numbers)
    
    while i < length:
        j = i + 1
        while j < length:
            if numbers[i] + numbers[j] == sum:
                return True
            j += 1
        i += 1
        
    return False
