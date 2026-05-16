def first_last(letter: str, st: str) -> bool:
    """"
    >>> first_last('a', 'abba')
    (0, 3)
    True
    >>> first_last('a', 'abbaaaab')
    (0, 6)
    True
    >>> first_last('a', 'a')
    (0, 0)
    True
    >>> first_last('a', 'spring')
    (None, None)
    False
    """
    if st.find(letter) < 0:
        print ((None, None)) # я просто хотел что бы он мне возращал мне одно и то же
        return False
    else:
        print ((st.find(letter), st.rfind(letter)))
        return True