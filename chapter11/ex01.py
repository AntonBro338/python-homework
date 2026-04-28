def histogram(string: str) -> dict[str, int]:
    """
    >>> histogram ("Гиппопотамус")
    {'Г': 1, 'и': 1, 'п': 3, 'о': 2, 'т': 1, 'а': 1, 'м': 1, 'у': 1, 'с': 1}
    >>> histogram ("Бронтазавр")
    {'Б': 1, 'р': 2, 'о': 1, 'н': 1, 'т': 1, 'а': 2, 'з': 1, 'в': 1}
    """
    hist = dict()
    for char in string:
        hist[char] = hist.get(char, 0) + 1
    return hist
