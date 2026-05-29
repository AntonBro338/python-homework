def useless(lst: list[int | float]) -> float:
    return max(lst) / len(lst) #тут когбду-то не понятно как переделывать это

# Тесты
print(useless([1, 5, 30]))
print(useless([19, 8.3, -4, 11, 0, 5]))
print(useless([-33, -0.05, -4.18, 11.2, 13.12, 55, 7.1]))