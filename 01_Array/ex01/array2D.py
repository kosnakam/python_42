
def slice_me(family: list, start: int, end: int) -> list:
    """This function is like a slice."""
    try:
        assert family != None and type(family) is list and type(start) is int and type(
            end) is int, "These arguments are not accepted."
        base_len = len(family[0])
        assert all(len(element) == base_len for element in family), "The lists are not the same size."

        print(f"My shape is : ({len(family)}, {base_len})")
        ret = family[start:end]
        print(f"My new shape is : ({len(ret)}, {base_len})")

    except AssertionError as e:
        print(f"Error(slice_me): {e}")
        return

    return ret
