def difference (l1: list[int], l2: list[int]) -> list[int]:
    """
    l1 - list containing non-repeated integer numbers
    l2 = list containing non-repeated integer numbers
    returns new list with  integer numers existing  in l1
    but non-existing  l2
    Examples: difference([1, 2, 3], [4, 3, 1])=> [2]
    difference([1, 2, 3], [4, 5, 6])=> [1, 2, 3]
    """
    return [num for num in l1 if num not in l2]