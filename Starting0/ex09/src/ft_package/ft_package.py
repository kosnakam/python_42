def count_in_list(lst: list, arg: str) -> int:
    """This function counts the number ob arg in lst"""
    return (sum(1 for element in lst if arg == element))
