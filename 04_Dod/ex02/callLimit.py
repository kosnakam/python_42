from typing import Any


def callLimit(limit: int):
    """Layer 1 The Factory."""
    count = 0

    def callLimiter(function):
        """Layer 2 The Decorator"""
        def limit_function(*args: Any, **kwds: Any):
            """Layer 3 The Wrapper"""
            nonlocal count
            if count < limit:
                function(*args, **kwds)
            else:
                print(f"Error: <function {function.__name__} \
at {hex(id(function))}> call too many times")
            count += 1
        return limit_function
    return callLimiter
