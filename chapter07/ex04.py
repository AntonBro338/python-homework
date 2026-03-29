def palindrom(word: str): 
    iters = len(word)//2 
    for i in range(iters): 
        if word[i] != word[-i - 1]:
            print (False)
            return False 
    print (True)
    return True 

while True:
    word = input('Введите слово для проверки на полиндром: ') #получаем слово на ввод
    print(f'{word} да, это полиндром' if palindrom(word) else f'{word} нет, это не палиндром') 
