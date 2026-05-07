import string
from lib import remove_metadata, histogram, parse_words, read_file

def analyze_book(filename: str):
    """Проанализировать книгу и вывести статистику"""
    print(f"Общее количество слов в книге: {len(parse_words(remove_metadata(read_file(filename))))}")
    print(f"Количество разных слов: {len(histogram(parse_words(remove_metadata(read_file(filename)))))}")
    print (f"Двадцать самых распространенных слов: { sorted(histogram(parse_words(remove_metadata(read_file(filename)))).items(), key=lambda x: x[1], reverse=True)[:20]}")

analyze_book("book.txt")