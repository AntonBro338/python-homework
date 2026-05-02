def anagrams(filename) -> dict [str, list[str]]:
  anagram_map = {}
  with open(filename) as word_list:
    for word in word_list:
      word = word.strip().lower()
      key = "".join(sorted(word))
      anagram_map.setdefault(key, []).append(word)
  return anagram_map

def print_sorted_anagrams(anagram_map: dict[str, list[str]]):
    items = list(anagram_map.items())
    anagram_items = [item for item in items if len(item[1]) > 1]
    anagram_items.sort(key=lambda item: len(item[1]), reverse=True)
    for key, group in anagram_items:
        print(f"'{key}': {group}")

print_sorted_anagrams(anagrams ('words.txt'))