import random
from lib import histogram

def choose_from_hist(hist: dict[str, int], n: int) -> str:
    pool = []
    for word, freq in hist.items():
        pool.extend([word] * freq)
    results = {word: 0 for word in hist.keys()}
    for i in range(n):
        results[random.choice(pool) if pool else ""] += 1
    for word, count in results.items():
        print(f"{word}: {count} раз ({count / n:.3%})")
    return random.choice(pool) if pool else ""


choose_from_hist(histogram(["а", "а", "б"]), 100000)
