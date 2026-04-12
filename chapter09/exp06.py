def is_anagram(str1, str2):
    cleaned_str1 = str1.lower().replace(' ', '')
    cleaned_str2 = str2.lower().replace(' ', '')
    if sorted(cleaned_str1) == sorted(cleaned_str2):
        return "анаграммом"
    else:
        return "НЕ анаграммом"


str1 = input('Первое слово: ')
str2 = input('Второе слово: ')

print(f'Слова {str1} и {str2} являются {is_anagram(str1, str2)}')
