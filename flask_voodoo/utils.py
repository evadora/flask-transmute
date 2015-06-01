def get_public_callables(obj):
    """
    return an iterator over all public callables of a function
    """
    for key in dir(obj):
        if key.startswith('_'):
            continue
        value = getattr(obj, key)
        if callable(value):
            yield key, value
