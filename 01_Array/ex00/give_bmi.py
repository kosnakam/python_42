import numpy


def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    try:
        assert len(height) == len(weight), "Lists of arguments must be the same size!"
        assert all(isinstance(element, (int, float)) for element in height), "Height lists of arguments has to have int or float!"
        assert all(isinstance(element, (int, float)) for element in weight), "Weight lists of arguments has to have int or float!"
        
        ret = None
        for h, w in zip(height, weight):
            ret.append(w/)



    except AssertionError as e:
        print(f"Error(give_bmi): {e}")
    return

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    return
