from lib import read_file, parse_words, remove_metadata

print (parse_words(remove_metadata(read_file('book.txt'))))

