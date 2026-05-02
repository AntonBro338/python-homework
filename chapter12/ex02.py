
def print_most_frequent(t: str):
    """
    >>> print_most_frequent ('полиграф')
    п 1
    о 1
    л 1
    и 1
    г 1
    р 1
    а 1
    ф 1
    """
    total = {}  # создаем словарь
    for a in t:  #
        if a.isalpha():  # приводим
            a_lower = a.lower()  #
            total[a_lower] = total.get(a_lower, 0) + 1  #
    total_list = list(total.items())  #
    sorted_total = sorted(total_list, key=lambda x: x[1])  #

    for b, c in sorted_total:  #
        print(f'{b} {c}')
