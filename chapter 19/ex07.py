def classify_words(words: list[str]) -> dict[str, list[str]]:
    result = {}
    for word in words:
        if word:
            first_letter = word[0].lower()
            if first_letter not in result:
                result[first_letter] = []
            result[first_letter].append(word)
    return result

print (classify_words (['EewwWrwrwrw', 'afhgfhfhh']))