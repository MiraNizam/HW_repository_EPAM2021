from typing import Callable
from functools import wraps


def make_key(args, kwargs):
    return args, sorted(kwargs.items())


def cache_deco(times: int = 1) -> Callable:
    """The parametrized decorator give out cached value up to `times` number only"""

    def wrapper(func):
        cache_data = {}

        @wraps(func)
        def inner(*args, **kwargs):
            key = make_key(args, kwargs)
            if key not in cache_data:
                result = func(*args, **kwargs)
                cache_data[key] = [result, times + 1]
            result, called = cache_data[key]
            if called == 0:
                return func(*args, **kwargs)
            else:
                cache_data[key][1] -= 1
                return result

        return inner

    return wrapper