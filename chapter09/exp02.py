def cumsum(t: list[int]):
    new_list = []
    accumulation_sum = 0
    for elements in t:
        accumulation_sum += elements
        new_list.append(accumulation_sum)
    return new_list

t = [1, 2, 3]
print (cumsum(t))
print (t) #поидее, новый список создал, слышал что result.append не создает нового списка, а изменяет сушествующий
