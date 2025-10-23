def count_in_list(lst: list, arg: str) -> int:
    return(sum(1 for arg in lst if arg == lst))
