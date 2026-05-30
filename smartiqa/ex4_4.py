def useless(lst: list[int | float]) -> float:
    """"
    >>> useless([1, 2, 3])
    1.0
    >>> useless([1, 5, 30])
    10.0
    """
    return max(lst) / len(lst) #тут когбду-то не понятно как переделывать это
