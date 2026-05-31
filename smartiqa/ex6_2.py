def slicer(tpl: tuple[int, ...], element: int) -> tuple[int, ...]:
    """"
    >>> slicer((1, 2, 3), 8)
    ()
    >>> slicer((1, 2, 3), 2)
    (2, 3)
    >>> slicer((1, 2, 8, 5, 1, 2, 9), 2)
    (2, 8, 5, 1, 2)
    >>> slicer((), 8)
    ()
    >>> slicer((2, 2), 2)
    (2, 2)
    """
    if element in tpl:
        if tpl.count(element) > 1:
            return tpl[tpl.index(element):tpl.index(element, tpl.index(element) + 1) + 1]
        else:
            return tpl[tpl.index(element):]
    else:
        return ()
