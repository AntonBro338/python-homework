def histogram(string: str) -> dict[str, int]:
    hist = dict()
    for char in string:
        hist[char] = hist.get(char, 0) + 1
    return hist
