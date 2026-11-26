def remove_duplicates(numbers: list[int]) -> list[int]:
    """
    Algorithm complexity O[N]
    returns new list containing all numbers from 'numbers' parameter
    except duplicates. The order should be kept
    Example:  'numbers' - [-1, 0, 100, -1, 20, 80, 20] the function should return
    new list [-1, 0, 100,  20, 80]
    """
    seen: set[int] = set()
    result: list[int] = []

    for num in numbers:
        if num not in seen:
            seen.add(num)
            result.append(num)

    return result
