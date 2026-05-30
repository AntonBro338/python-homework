def slicer(any_tuple: tuple[int, ...], element: int) -> tuple[int | None, ...]:
    if element in any_tuple:
        if any_tuple.count(element) > 1:
            return any_tuple[any_tuple.index(element):any_tuple.index(element, any_tuple.index(element) + 1) + 1]
        else:
            return any_tuple[any_tuple.index(element):]
    else:
        return ()

print(slicer((1, 2, 3), 8))
print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
print(slicer((1, 2, 8, 5, 1, 2, 9), 8))