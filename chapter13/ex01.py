import string

def read_file(filename: str) -> list[str]:
    """Прочитать файл построчно в список"""
    with open(filename) as file:
        return [line.strip() for line in file]

def parse_words(lines: list[str]) -> list[str]:
    """Разбить список строк на слова"""
    all_words = []
    for line in lines:
        parts = line.split()
        for word in parts:
            word.lower()
            word.strip(string.punctuation)
            all_words.append(word)
    return all_words


print (parse_words(read_file('words.txt')))