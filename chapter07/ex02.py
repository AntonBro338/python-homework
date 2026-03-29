product = 1 
while True :
    line = input ('> ')
    number = int(line)
    if number < 0:
        print ("Пропускаем отрицательное число")
    elif number == 0:
        product = product * number 
        print ("Произведение на данный момент:", product)
        break
        continue
    if number > 0:
        product = product * number 
        print ("Произведение на данный момент:", product)
