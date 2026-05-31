def del_from_tuple(tpl: tuple[int, ...], elem: int) -> tuple[int, ...]:
    """
    >>> del_from_tuple((1, 1, 2, 3), 3)
    (1, 1, 2)
    >>> del_from_tuple((), 0)
    ()
    >>> del_from_tuple((1, 1, 2, 3), 1)
    (1, 2, 3)
    """
    if elem in tpl:
        new_tpl = tpl[:tpl.index(elem)] + tpl[tpl.index(elem) + 1:]
        return new_tpl
    return tpl

