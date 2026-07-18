from collections import Counter

def count_it(sequence: str) -> dict:
    """"
    >>> count_it ("12233344455555666666")
    {6: 6, 5: 5, 3: 3}
    >>> count_it ("")
    {}
    """
    return dict(Counter(int(num) for num in sequence).most_common(3))
