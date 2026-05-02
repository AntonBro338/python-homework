def sumall(*args: int) -> int:
    """
        >>> sumall(1, 2, 3)
        6
        >>> sumall(5)
        5
        >>> sumall() #если не давать аргументов то выдаст ноль
        0
        >>> sumall(-1, 1, 5)
        5
    """
    return sum(args)

