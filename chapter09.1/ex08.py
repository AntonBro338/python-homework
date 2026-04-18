def is_palindrome(str):
    return str == str[::-1]

def check_odometer(num):
    """ Проверяем на условия задачи """
    str0 = str(num).zfill(6)
    str1 = str(num + 1).zfill(6)
    str2 = str(num + 2).zfill(6)
    str3 = str(num + 3).zfill(6)
    cond1 = is_palindrome(str0[2:])
    cond2 = is_palindrome(str1[1:])
    cond3 = is_palindrome(str2[1:5])
    cond4 = is_palindrome(str3)
    return cond1 and cond2 and cond3 and cond4

def odometer_reading():
    """ Ищет и выводит все шестизначные числа """
    results = []
    for mileage in range(100000, 1000000):
        if check_odometer(mileage):
            results.append(mileage)
    return results

print(f"Исходное показание пробега: {odometer_reading()}") # оба значения подходят под условия задачи, 
но второе когбуд-то меньше подходит если его дальше по условиям провести, больше палиндром получается
