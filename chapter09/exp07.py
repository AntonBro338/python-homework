def has_duplicates(t):
    t = sorted(t)
    for i in range(len(t) - 1):
        if t[i] == t[i + 1]:
            return True
    return False

user_input = input("Введите список чисел через пробел: ")
t = list(map(int, user_input.split()))
print(has_duplicates(t))
