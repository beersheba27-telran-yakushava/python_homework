def min_max_average (l1: list[int]) -> tuple[int, int, float]:
    if not l1:
        raise ValueError("Сonnot process an empty list")

    return min(l1), max(l1), sum(l1) / len(l1)
