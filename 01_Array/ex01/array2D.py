
def slice_me(family: list, start: int, end: int) -> list:
    """This function is like a slice."""
    try:
        assert type(family) is list and type(start) is int and type(
            end) is int, "These arguments are not accepted."
        assert len(family) > end and len(
            family) >= start, "The lists are not the same size."

        ret = family[start:end]

    except AssertionError as e:
        print(f"Error(slice_me): {e}")

    return ret
