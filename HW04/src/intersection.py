def intersection (l1: list[int], l2: list[int]) -> list[int]:
    """
    l1 - list containing non-repeated integer numbers
    l2 = list containing non-repeated integer numbers
    returns new list with integer numers existing in both input lists
    Examples: intersection([1, 2, 3], [4, 3, 1])=> [1, 3]
    intersection([1, 2, 3], [4, 5, 6])=> [];
    """
    return [num for num in l1 if num in l2]
