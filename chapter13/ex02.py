import string


def read_file(filename: str) -> list[str]:
    """Прочитать файл построчно в список"""
    with open(filename, 'r', encoding='utf-8') as file:
        return [line for line in file]


def remove_metadata(lines: list[str]) -> list[str]:
    """Удаляет строки до начала книги и после её завершения"""
    header_end = '*** START OF THE PROJECT'
    footer_start = '*** END OF THE PROJECT'
    start_idx = 0
    end_idx = len(lines)
    for i, line in enumerate(lines):
        if line.startswith(header_end):
            start_idx = i + 1
        if line.startswith(footer_start):
            end_idx = i
    return lines[start_idx:end_idx]


def parse_words(lines: list[str]) -> list[str]:
    """Разбить список строк на слова"""
    all_words = []
    for line in lines:
        parts = line.split()
        for word in parts:
            word = word.lower() #сли без word то работает, но тогда не приводит к одному регистру
            word = word.strip(string.punctuation)
            all_words.append(word)
    return all_words

print (parse_words(remove_metadata(read_file('book.txt'))))

