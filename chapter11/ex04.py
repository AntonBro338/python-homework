def has_duplicates(t: list) -> bool:
    """
    >>> has_duplicates (['1', '2', '3'])
    'Нет дубликата'

    >>> has_duplicates (['1', '2', '2'])
    'Есть дубликат'
    """
    word = {}
    for sort in t:
        if sort in word:
            return "Есть дубликат"
        word[sort] = True
    return "Нет дубликата"
