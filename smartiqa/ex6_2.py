def slicer(any_tuple: tuple[int, ...], element: int) -> tuple[int | None, ...]:
    """"
    >>> slicer((1, 2, 3), 8)
    ()
    >>> slicer((1, 2, 3), 2)
    (2, 3)
    """
    if element in any_tuple:
        if any_tuple.count(element) > 1:
            return any_tuple[any_tuple.index(element):any_tuple.index(element, any_tuple.index(element) + 1) + 1]
        else:
            return any_tuple[any_tuple.index(element):]
    else:
        return ()
