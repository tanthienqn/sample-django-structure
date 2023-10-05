import time
from functools import wraps


class Util:

    @classmethod
    def time_used(cls, fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = fn(*args, **kwargs)
            end = time.time()
            print(f"Function {fn.__name__!r} executed in {(end - start):.4f}s")
            return result

        return wrapper
