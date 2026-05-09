import random
from lib import histogram

def choose_from_hist(hist: dict[str, int]) -> str:
    """
    >>> choose_from_hist({})
    Traceback (most recent call last):
    ...
    IndexError: Cannot choose from an empty sequence
    """
    pool = []
    for word, freq in hist.items():
        pool.extend([word] * freq)
    return random.choice(pool)


def test(hist: dict[str, int], n: int) -> dict[str, int]:
    """
    >>> n = 10000
    >>> results = test({'а': 2, 'б': 1}, n)
    >>> assert 0.63 <= results['а'] / n <= 0.69
    >>> assert 0.30 <= results['б'] / n <= 0.37
    """
    results = {word: 0 for word in hist.keys()}
    for i in range(n):
        results[choose_from_hist(hist)] += 1
    return results
    # for word, count in results.items():
    #     print(f"{word}: {count} раз, ({count / n:.3%})")
