from typing import Any

def tpl_sort(tpl: tuple[Any, ...]) -> tuple[Any, ...]:
    if all(isinstance(element, int) for element in tpl):
        return tuple(sorted(tpl))
    return tpl

# Тесты
print(tpl_sort((5, 5, 3, 1, 9)))
print(tpl_sort((5, 5, 2.1, '1', 9)))