def del_from_tuple(tpl, elem) -> tuple[int, ...]:
    """
    >>> del_from_tuple((1, 1, 2, 3), 3)
    (1, 1, 2)
    >>> del_from_tuple((0,), 0)
    ()
    """
    if elem in tpl:
        elem_index = tpl[:tpl.index(elem)] + tpl[tpl.index(elem) + 1:]
        return elem_index # elem - это индекс значения которое убирают
    return tpl

