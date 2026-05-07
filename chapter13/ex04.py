import string
from lib import read_file, parse_words, remove_metadata
from typing import Dict

def find_unknown_words(book_file: str, words_file: str) -> Dict[str, int]:
    """Выдает слова которых не было в списке"""
    book_words = parse_words(remove_metadata(read_file(book_file)))
    official_words = {
        word.lower().strip(string.punctuation)
        for word in read_file(words_file)}
    unknown: Dict[str, int] = {}
    for word in book_words:
        if word not in official_words:
            unknown[word] = unknown.get(word, 0) + 1
    return unknown

print (find_unknown_words("book.txt", "words.txt"))


