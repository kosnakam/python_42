def ft_tqdm(lst: range) -> None:
    """
    Decorate an iterable object, returning an iterator which acts exactly
    like the original iterable, but prints a dynamically updating
    progressbar every time a value is requested.
    """
    n = len(lst)
    bar_len = 47
    for i in lst:
        percent = (i + 1) / n
        num_hash = int(bar_len * percent)
        bar = '█' * num_hash + ' ' * (bar_len - num_hash)
        print(f"\r{percent*100:.0f}%|{bar}| {i}/{n}", end='')
        yield i
    print(f"\r{percent*100:.0f}%|{bar}| {i + 1}/{n}", end='')
