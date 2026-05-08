import string

def read_file(filename: str) -> list[str]:
    r""" # я не знаю что это за r, но без нее он жалуется на кавычки
    >>> read_file('words_2.txt')
    ['book', '*** START OF THE PROJECT', 'look', 'dag', 'dog bag', '', 'bog', 'vog', 'z', 'gl hf', 'U2', '*** END OF THE PROJECT', 'gg', 'wp']
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file]

def parse_words(lines: list[str]) -> list[str]:
    r"""
    >>> parse_words (read_file('words_2.txt'))
    ['book', '***', 'START', 'OF', 'THE', 'PROJECT', 'look', 'dag', 'dog', 'bag', 'bog', 'vog', 'z', 'gl', 'hf', 'U2', '***', 'END', 'OF', 'THE', 'PROJECT', 'gg', 'wp']
    """
    all_words = []
    for line in lines:
        parts = line.split()
        for word in parts:
            word.lower()
            word.strip(string.punctuation)
            all_words.append(word)
    return all_words
