from typing import Callable


def cache(func: Callable) -> Callable:
    func._cache = {}

    def wrapper(*args, **kwargs) -> Callable:
        key = (args, tuple(sorted(kwargs)))
        if key in func._cache:
            print("Getting from cache")
            return func._cache[key]
        else:
            print("Calculating new result")
            result = func(*args, **kwargs)
            func._cache[key] = result
            return result
    return wrapper
