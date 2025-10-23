def count_in_list(lst: list, arg: str) -> int:
    return(sum(1 for element in lst if arg == element))
