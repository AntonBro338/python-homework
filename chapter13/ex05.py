import random
from lib import histogram

def choose_from_hist(hist: dict[str, int]) -> str:
    pool = []
    for word, freq in hist.items():
        pool.extend([word] * freq)
    for i in range(9):
        print(random.choice(pool) if pool else "")
    return random.choice(pool) if pool else ""

choose_from_hist(histogram(["а", "а", "б"]))
