from typing import Any

def change(lst: list[Any]) -> list[Any]:
    """"
    >>> change([1, 2, 3])
    [3, 2, 1]
    >>> change(['н', 'л', 'о', 'с'])
    ['с', 'л', 'о', 'н']
    """
    if len(lst):
        lst[0], lst[-1] = lst[-1], lst[0]
    return lst
