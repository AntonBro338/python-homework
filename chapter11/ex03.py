import doctest
import typing

K = typing.TypeVar("K")
V = typing.TypeVar("V")


def invert_dict(d: dict[K, V]) -> dict[V, list[K]]:
    """
    >>> invert_dict ({"ключ": 'Бегемотикус'})
    {'Бегемотикус': ['ключ']}

    >>> invert_dict({'a': 1, 'b': 1, 'c': 2})
    {1: ['a', 'b'], 2: ['c']}
    """
  
    inverse = dict()
    for key in d:
        value = d[key]
        inverse.setdefault(value, []).append(key)

    return inverse


doctest.testmod()
