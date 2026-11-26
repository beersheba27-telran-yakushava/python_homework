def symmetric_difference (l1: list[int], l2: list[int]) -> list[int]:
    """
    l1 - list containing non-repeated integer numbers
    l2 = list containing non-repeated integer numbers
    returns new list with  integer numers existing  in either list but not in both
    Examples: symmetric_difference([1, 2, 3], [4, 3, 1])=> [2, 4]
    symmetric_difference([1, 2, 3], [4, 5, 6])=> [1, 2, 3, 4, 5, 6]
    """
    l3: list[int] = [num for num in l1 if num not in l2]
    l4: list[int] = [num for num in l2 if num not in l1]

    return l3 + l4
