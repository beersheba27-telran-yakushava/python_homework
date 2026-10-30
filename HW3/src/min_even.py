def min_even (numbers: list[int]):
    """
    "numbers" - list with int numbers
    returns minimal even number
    assumption: at least one even number exists in "numbers"
    no need to check that assumption (usually the assumptions are never checked ) 
    example: min_even (-10001, 10, 20, 8, -7) => 8
    """ 
    min_num = None
    index = 0
    
    while index < len(numbers):
        current = numbers[index]
        if current % 2 == 0:
            if min_num is None or current < min_num:
                min_num = current
        index += 1
        
    return min_num
