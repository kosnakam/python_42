
def square(x: int | float) -> int | float:
    """A function calculating the square."""
    return x ** 2


def pow(x: int | float) -> int | float:
    """A function calculating the pow."""
    return x ** x


def outer(x: int | float, function) -> object:
    """Outer funciton."""
    count = 0

    def inner() -> float:
        """Inner function."""
        nonlocal x, count
        count += 1
        x = function(x)
        return x

    return inner
