from lib import remove_metadata, histogram, parse_words, read_file

def analyze_book(filename: str):
    r"""
    >>> analyze_book("words_2.txt")
    Общее количество слов в книге: 10
    Количество разных слов: 10
    Двадцать самых распространенных слов: [('look', 1), ('dag', 1), ('dog', 1), ('bag', 1), ('bog', 1), ('vog', 1), ('z', 1), ('gl', 1), ('hf', 1), ('U2', 1)]
    """
    print(f"Общее количество слов в книге: {len(parse_words(remove_metadata(read_file(filename))))}")
    print(f"Количество разных слов: {len(histogram(parse_words(remove_metadata(read_file(filename)))))}")
    print (f"Двадцать самых распространенных слов: { sorted(histogram(parse_words(remove_metadata(read_file(filename)))).items(), key=lambda x: x[1], reverse=True)[:20]}")
