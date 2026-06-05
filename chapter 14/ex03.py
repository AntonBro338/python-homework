import shelve

def sum_baks() -> None:
    try:
        with shelve.open("expenses") as baks:
            if "total" not in baks:
                baks["total"] = 0
            print(f"Текущие расходы: {baks['total']} руб.")
            while True:
                try:
                    baks["total"] += int(input("Введите потраченную сумму в рублях: "))
                    print(f"Текущие расходы: {baks['total']} руб.")
                except ValueError:
                    print("Вы ввели неправильное значение")
    except KeyboardInterrupt:
        pass


sum_baks ()