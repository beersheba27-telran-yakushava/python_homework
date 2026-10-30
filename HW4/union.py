def union (l1: list[int], l2: list[int]) -> list[int]:
    """
    l1 - list containing non-repeated integer numbers
    l2 = list containing non-repeated integer numbers
    returns new list with  integer numers existing  in ether list or both
    Result list shouldn't contain repeated numbers
    Examples: union([1, 2, 3], [4, 3, 1])=> [1, 2, 3, 4]
    union([1, 2, 3], [4, 5, 6])=> [1, 2, 3, 4, 5, 6]
    """
    l3: list[int] = [num for num in l2 if num not in l1]

    return l1 + l3
