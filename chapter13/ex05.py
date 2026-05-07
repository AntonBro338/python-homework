import random
from typing import Dict
from lib import histogram

def choose_from_hist(hist: Dict[str, int]) -> str:
    pool = []
    for word, freq in hist.items():
        pool.extend([word] * freq)
    for i in range(10):
        print(random.choice(pool) if pool else "")
    return random.choice(pool) if pool else ""

choose_from_hist(histogram(["а", "б", "б"]))
