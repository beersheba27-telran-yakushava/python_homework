def remove_positive_greater_or_negative_less(numbers:list[int], positive_lim: int, negative_lim: int) -> list[int]:
    """
    numbers - list with integer numbers
    returns new list containing all numbers from the input list
    except the positive ones greater than 'positive_lim' and the negative ones
    less than 'negative_lim'
    Example: remove_positive_greater_or_negative_less([1, 2, 11, -3, 10, 15], 10, -3)
    => [1, 2, -3, 10]
    """
    return [num for num in numbers if num <= positive_lim and num >= negative_lim]
