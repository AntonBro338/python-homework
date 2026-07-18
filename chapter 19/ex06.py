from collections import Counter

def count_it(sequence: str) -> dict:
    return dict(Counter(int(num) for num in sequence).most_common(3))

print (count_it ("1111111112345666666"))