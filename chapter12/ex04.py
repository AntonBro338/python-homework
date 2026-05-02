def anagrams(word_list: list[str]) -> dict[str, list[str]]:
    anagram_map = {}
    for word in word_list:
        word = word.strip().lower()
        key = "".join(sorted(word))
        anagram_map.setdefault(key, []).append(word)
    return anagram_map

def has_metathetic_pairs(word_list: list[str]) -> list[tuple[str, str]]:
    """
    Находит все метатетические пары в списке слов.
    """
    anagram_groups = anagrams(word_list)
    metathetic_pairs = []
    for key, words in anagram_groups.items():
        if len(words) < 2:
            print ("Нет, это не подходит")
            continue
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                word1, word2 = words[i], words[j]
                if is_metathetic(word1, word2):
                    metathetic_pairs.append((word1, word2))
    return metathetic_pairs

def is_metathetic(word1: str, word2: str) -> bool:
    """
    Проверяет, образуют ли два слова метатетическую пару.
    """
    if len(word1) != len(word2):
        return False
    diff_positions = []
    for positions, (character_positions1, character_positions2) in enumerate(zip(word1, word2)):
        if character_positions1 != character_positions2:
            diff_positions.append(positions)
    if len(diff_positions) != 2:
        return False
    positions1, positions2 = diff_positions
    return word1[positions1] == word2[positions2]

print (has_metathetic_pairs (["converse", "conserve"]))
