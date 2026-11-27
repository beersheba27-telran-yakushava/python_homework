def get_occurrences_counts(strings: list[str]) -> list[str]:
    """
    returns list of ordered strings
    each output string should have the following structure
    <string from the input list>=><occurrencies count>
    The output list should be sorted by two criteria:
    descending order of counts and ascending order of strings themselves
    example: input list is ["lmn", "vs", "y", "y", "ab", "a", "lmn", "lmn"]
     the output list is ["lmn=>3", "y=>2", "a=>1", "ab=>1", "vs=>1"]
    """
    counts: dict[str, int] = {}
    for string in strings:
        counts[string] = counts.get(string, 0) + 1

    ordered_strings = sorted(counts, key=lambda string: (-counts[string], string))
    return [f"{string}=>{counts[string]}" for string in ordered_strings]
