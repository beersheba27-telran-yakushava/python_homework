def update_with_first_removing[K, V](cache: dict[K, V], entry: tuple[K, V], limit: int) -> None:
    """
    if "cache" dictionary already has a key-value pair with first item of a given "entry" as the key
    the key-value pair will be updated with second item of the entry 
    if "cache" dictionary doesn't have a such key-value pair the given "entry" should be added.
    But if the adding new pair will exeed a "limit" the first pair (isertion order) should be deleted
    Example: "cache" - {"a":10, "b":20, "c":30} update_with_first_removing(cache, ("a", 40),3) will update pair with key "a"
    and cache will be {"a":40, "b":20, "c":30}; update_with_first_removing(cache, ("d", 40),3) will add new pair,but
    remove the first one, so cache will be { "b":20, "c":30, "d":40}
    """
    key, value = entry
    if key in cache:
        cache[key] = value
        return

    cache[key] = value
    if len(cache) > limit:
        oldest_key = next(iter(cache))
        del cache[oldest_key]
