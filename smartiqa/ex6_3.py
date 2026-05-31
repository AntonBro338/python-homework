from typing import Sequence

def sieve(lst: Sequence[int]) -> tuple[int, ...]:
    """
    >>> sieve([1, 2, 3, 3, 2])
    (2, 3, 1)
    >>> sieve([])
    ()
    """
    unique = []
    for item in reversed(lst):
        if item not in unique:
            unique.append(item)
    return tuple(unique)

