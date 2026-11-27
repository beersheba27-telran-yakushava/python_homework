from HW12.src.update_with_first_removing import update_with_first_removing

def test_adds_entry_to_empty_cache() -> None:
    cache: dict[str, int] = {}
    result = update_with_first_removing(cache, ("a", 10), 2)

    assert result is None
    assert list(cache.items()) == [("a", 10)]

def test_adds_entry_without_exceeding_limit() -> None:
    cache: dict[str, int] = {"a": 10}
    result = update_with_first_removing(cache, ("b", 20), 3)

    assert result is None
    assert list(cache.items()) == [("a", 10), ("b", 20)]

def test_updates_existing_entry_without_changing_order() -> None:
    cache: dict[str, int] = {"a": 10, "b": 20, "c": 30}
    result = update_with_first_removing(cache, ("b", 25), 3)

    assert result is None
    assert list(cache.items()) == [("a", 10), ("b", 25), ("c", 30)]

def test_removes_oldest_entry_when_limit_is_exceeded() -> None:
    cache: dict[str, int] = {"a": 10, "b": 20, "c": 30}
    result = update_with_first_removing(cache, ("d", 40), 3)

    assert result is None
    assert list(cache.items()) == [("b", 20), ("c", 30), ("d", 40)]
