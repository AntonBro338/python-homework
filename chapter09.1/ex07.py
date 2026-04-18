
def _3_double(word):
    """Проверяет, есть ли в слове три дубля подряд."""
    word = word.lower()
    double = 0
    i = 0
    while i < len(word) - 1:
        if word[i] == word[i + 1]:
            double += 1
            i += 2
            if double == 3:
                return True
        else:
            double = 0
            i += 1
    return False

def words_in_file(files):
    """Ишет в файле слова"""
    matching_words = []
    with open('words.txt') as word:
        line_num = 1
        for line in word:
            word = line.strip()
            if _3_double (word):
                matching_words.append((word, line_num))
            line_num += 1
    return matching_words

print (words_in_file('words.txt'))
