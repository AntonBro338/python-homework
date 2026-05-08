from lib import read_file, parse_words

def remove_metadata(lines: list[str]) -> list[str]:
    r"""
    >>> print (remove_metadata(read_file('words_2.txt')))
    ['look', 'dag', 'dog bag', '', 'bog', 'vog', 'z', 'gl hf', 'U2']
    """
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

print (parse_words(remove_metadata(read_file('book.txt'))))

