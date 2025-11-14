from typing import Any

def ft_mean(args):
    try:
        assert len(args) != 0
        return sum(args) / len(args)

    except AssertionError:
        print("ERROR")
        return


def ft_median(args):
    try:
        assert len(args) != 0
        index, array = len(args) / 2, sorted(args)
        if index % 2 != 0:
            return array[int(index)]
        else:
            return (array[int(index)] + array[int(index) + 1]) / 2

    except AssertionError:
        print("ERROR")
        return


def ft_quartile(args):
    try:
        assert len(args) != 0
        n = len(args)
        array, n4, n2 = sorted(args), n / 4, n / 2

        if n2 % 1 != 0:
            n4 = (int(n2) + 1) / 2
            if n4 % 1 != 0:
                return [float(array[int(n4)]), float(array[int(n4) + int(n2)])]
            else:
                return [float((array[int(n4) - 1] + array[int(n4)]) / 2), float((array[n - int(n4) - 1] + array[n - int(n4)]) / 2)]
        else:
            n4 = int(n2) / 2
            if n4 % 1 != 0:
                return [float(array[int(n4)]), float(array[int(n4) + int(n2)])]
            else:
                return [float((array[int(n4) - 1] + array[int(n4)]) / 2), float((array[n - int(n4) - 1] + array[n - int(n4)]) / 2)]

    except AssertionError:
        print("ERROR")
    return


def ft_std(args):
    try:
        assert len(args) != 0
        # print(args)
    except AssertionError:
        print("ERROR")
    return


def ft_var(args):
    try:
        assert len(args) != 0
        # print(args)
    except AssertionError:
        print("ERROR")
    return


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    try:
        assert all(isinstance(arg, (int, float)) for arg in args), "TypeError"
        assert all(isinstance(value, (str)) for value in kwargs.values()), "TypeError"
        array = {
            "mean": ft_mean,
            "median": ft_median,
            "quartile": ft_quartile,
            "std": ft_std,
            "var": ft_var
        }
        for value in kwargs.values():
            if value in array:
                print(f"{value} : {array[value](args)}")
                # array[value](args)

        return
    except AssertionError as e:
        print(f"Error(ft_statistics): {e}")
