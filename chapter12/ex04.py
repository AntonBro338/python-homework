def find_metathetic_pairs(anagram_map: dict[str, list[str]]) -> list[tuple[str, str]]:
    """
    Находит все метатетические пары внутри групп анаграмм.

    Args:
        anagram_map: словарь анаграмм (ключ — отсортированные буквы, значение — список слов).

    Returns:
        Список кортежей — метатетических пар.
    """
    metathetic_pairs = []

    # Обрабатываем каждую группу анаграмм
    for key, words in anagram_map.items():
        if len(words) < 2:  # если в группе меньше 2 слов, пропускаем
            continue

        # Сравниваем все пары слов в группе
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                word1, word2 = words[i], words[j]
                if is_metathetic(word1, word2):
                    metathetic_pairs.append((word1, word2))

    return metathetic_pairs

def is_metathetic(word1: str, word2: str) -> bool:
    """
    Проверяет, образуют ли два слова метатетическую пару.

    Args:
        word1, word2: два слова одинаковой длины.

    Returns:
        bool: True, если слова образуют метатетическую пару.
    """
    if len(word1) != len(word2):
        return False

    # Находим позиции, где буквы отличаются
    diff_positions = []
    for pos, (c1, c2) in enumerate(zip(word1, word2)):
        if c1 != c2:
            diff_positions.append(pos)

    # Условие метатетической пары: ровно два отличия, и буквы поменялись местами
    if len(diff_positions) != 2:
        return False

    pos1, pos2 = diff_positions
    return word1[pos1] == word2[pos2] and word1[pos2] == word2[pos1]