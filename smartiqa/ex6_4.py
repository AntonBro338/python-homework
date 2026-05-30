def del_from_tuple(tpl, elem) -> tuple[int, ...]:
    if elem in tpl:
        elem_index = tpl[:tpl.index(elem)] + tpl[tpl.index(elem) + 1:]
        return elem_index # elem - это индекс значения которое убирают
    return tpl

print(del_from_tuple((1, 1, 2, 3), 3))
print(del_from_tuple((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2, 4, 2), 3))
print(del_from_tuple((2, 4, 6, 6, 4, 2), 9))