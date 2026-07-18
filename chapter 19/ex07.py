def classify_words(words: list[str]) -> dict[str, list[str]]:
    """
    >>> classify_words (['EewwWrwrwrw', 'afhgfhfhh'])
    {'e': ['EewwWrwrwrw'], 'a': ['afhgfhfhh']}
    >>> classify_words ([])
    {}
    """
    result = {}
    for word in words:
        if word:
            first_letter = word[0].lower()
            if first_letter not in result:
                result[first_letter] = []
            result[first_letter].append(word)
    return result
