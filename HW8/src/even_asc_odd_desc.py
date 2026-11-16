def even_asc_odd_desc(numbers: list[int]) -> list[int]:
    """
    returns new list of numbers sorted in the following order:
    The even numbers ordered by ascending order reside before odd numbers ordered by descending order
    For example, even_asc_odd_desc([-3, -10, 12, 3, -21, 6, 21, 5, 4 ]) returns [-10, 4, 6, 12, 21, 5, 3, -3, -21]
    """
    return sorted(numbers, key=lambda n: (n % 2, n if n % 2 == 0 else -n))
