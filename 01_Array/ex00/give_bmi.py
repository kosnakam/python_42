def give_bmi(
        height: list[int | float], weight: list[int | float]
        ) -> list[int | float]:
    """This function return the bmi list."""
    try:
        assert type(height) is list and type(weight
                                             ) is list, "Arguments error."
        assert len(height) == len(
            weight
            ), "Lists of arguments must be the same size!"
        assert all(
            isinstance(element, (int, float)) for element in height
            ), "Height lists of arguments has to have int or float!"
        assert all(
            isinstance(element, (int, float)) for element in weight
            ), "Weight lists of arguments has to have int or float!"

        ret = []
        for h, w in zip(height, weight):
            ret.append(w/pow(h, 2))

    except AssertionError as e:
        print(f"Error(give_bmi): {e}")
        return None
    return ret


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """This function compare bmi and oranges."""
    try:
        assert type(bmi) is list, "The type of Bmi must be ListType!"
        assert type(limit) is int, "The second argument must be of type int!"
        assert all(
            isinstance(element, (float, int)) for element in bmi
            ), "Height lists of arguments has to have int or float!"

        ret = []
        for element in bmi:
            ret.append(True if element > limit else False)

    except AssertionError as e:
        print(f"Error(apply_limit): {e}")
        return None
    return ret
