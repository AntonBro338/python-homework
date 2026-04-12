import random 

def has_duplicates(t):
    t = sorted(t)
    for i in range(len(t) - 1):
        if t[i] == t[i + 1]:
            return True
    return False

def generate_birthdays(students):
    """Генерирует список из students случайных дней рождения (от 1 до 365)."""
    return [random.randint(1, 365) for _ in range(students)]

def birthday_probability(students=23, simulations=10000):
    """Оцениваем вероятность совпадения"""
    count_matches = 0
    for _ in range(simulations):
        birthdays = generate_birthdays(students)
        if has_duplicates(birthdays):
            count_matches += 1
    probability = (count_matches / simulations) * 100
    return probability

students = 23
simulations = 10000
probability = birthday_probability(students, simulations)

print(f"Парадокс дней рождения")
print(f"Количество студентов: {students}")
print(f"Количество симуляций: {simulations}")
print(f"Вероятность совпадения дней рождения: {probability}%")
