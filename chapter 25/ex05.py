def avoids(word: str, forbidden: str) -> bool:
    return set(word).issubset(set(word) - set(forbidden))