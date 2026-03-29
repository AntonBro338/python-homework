def print_n (string, n):
    while n <= 0:
        return # если убрать return получится бесконечная рекурсия
    print (string)
    print_n (string, n-1)
print_n ("ben", 5)
