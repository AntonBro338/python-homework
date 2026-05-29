def all_eq(lst: list[str]) -> list[str]:
     return [item.ljust(len(max(lst, key=lambda x: len(x))), '_') for item in lst]


# Тесты
print(all_eq(['крот', 'белка', 'выхухоль']))
print(all_eq(['a', 'aa', 'aaa', 'aaaa']))
print(all_eq(['qweasdqweas', 'q', 'rteww', 'ewqqqqq']))