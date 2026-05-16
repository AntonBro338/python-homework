from collections import Counter

def top3(st: str) -> list[tuple[str, int]]:
    return Counter(st.lower().replace(' ', '')).most_common(30)

# Тесты
print(top3('Улыбкой ясною природа Сквозь сон встречает утро года Синея блещут небеса. Еще прозрачные, леса'))
print(top3(''))
print(top3('Голова думала'))