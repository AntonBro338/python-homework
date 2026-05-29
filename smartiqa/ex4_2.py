from typing import Any

def change(lst: list[Any]) -> list[Any] :
    if len(lst) >= 2:
        lst[0], lst[-1] = lst[-1], lst[0]
    return lst

# Тесты
print(change([1, 2, 3]))
print(change([1, 2, 3, 4, 5]))
print(change(['н', 'л', 'о', 'с']))