def int_reverse(num: int) -> str:
    """
    returns string containing digits  of integer number "num" in reversed order
    if "num" contains only one digit it will return the same digit but as a string
    examples: int_reverse(10) -> "01"; int_reverse(1) -> "1";int_reverse(702) -> "207"
    """
    return str(num)[::-1]

def create_palindromic_list(start: int, stop: int) -> list[int]:
    """
    start, stop are integer numbers
    returns list containing all palindromic numbers in the range from "start" to "stop" 
    note: "start" may be less than "stop"
    requirement: to use "int_reverse" function
    """  
    result: list[int] = []
    step: int = 1 if start < stop else -1

    for num in range(start, stop+step, step):
        if int_reverse(num) == str(num): result.append(num)

    return result
