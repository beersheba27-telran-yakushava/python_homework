def min_even (numbers: list[int]) -> int | None:
    """
    "numbers" - list with int numbers
    returns minimal even number
    assumption: at least one even number exists in "numbers"
    no need to check that assumption (usually the assumptions are never checked ) 
    example: min_even (-10001, 10, 20, 8, -7) => 8
    """
    min_even_num = None

    for num in numbers:
        if num % 2 == 0 and (min_even_num is None or num < min_even_num):
            min_even_num = num
        
    return min_even_num
