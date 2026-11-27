def get_counts_strings(strings: list[str]) -> dict[int, list[str]] :
    """
    returns dictionary with an occurrence count as a key and sorted list of
    strings with the count
    example:  input list is ["lmn", "vs", "y", "y", "ab", "a", "lmn", "lmn"],
    output dict is {3:["lmn"], 2:["y"], 1:["a","ab","vs"]} 
    """
    counts: dict[str, int] = {}
    for string in strings:
        counts[string] = counts.get(string, 0) + 1

    grouped: dict[int, list[str]] = {}
    for string, count in counts.items():
        grouped.setdefault(count, []).append(string)

    for group in grouped.values():
        group.sort()

    return grouped
