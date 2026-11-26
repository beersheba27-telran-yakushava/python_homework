def move_max_to_end(l1: list[int]) -> None:
    if not l1:
        raise ValueError("Сonnot process an empty list")

    max_value: int = max(l1)

    l1.remove(max_value)
    l1.append(max_value)
