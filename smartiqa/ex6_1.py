from typing import Any

def tpl_sort(tpl: tuple[Any, ...]) -> tuple[Any, ...]:
    """"
    >>> tpl_sort((5, 5, 3, 1, 9))
    (1, 3, 5, 5, 9)
    >>> tpl_sort((5, 5, 2.1, '1', 9))
    (5, 5, 2.1, '1', 9)
    """
    if all(isinstance(element, int) for element in tpl):
        new_tuple = sorted(tpl)
        return tuple(new_tuple)
    return tpl
