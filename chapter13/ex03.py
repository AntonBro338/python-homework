import string
from ex02 import remove_metadata

def read_file(filename: str) -> list[str]:
    """Прочитать файл построчно в список"""
    with open(filename, 'r', encoding='utf-8') as file:
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

def histogram(words: list[str]) -> dict[str, int]:
    word_list = {}
    for word in words:
        word_list[word] = word_list.get(word, 0) + 1
    return word_list

def analyze_book(filename: str):
    """Проанализировать книгу и вывести статистику"""
    print(f"Общее количество слов в книге: {len(parse_words(remove_metadata(read_file(filename))))}")
    print(f"Количество разных слов: {len(histogram(parse_words(remove_metadata(read_file(filename)))))}")
    print (f"Двадцать самых распространенных слов: { sorted(histogram(parse_words(remove_metadata(read_file(filename)))).items(), key=lambda x: x[1], reverse=True)[:20]}")

analyze_book("book.txt")