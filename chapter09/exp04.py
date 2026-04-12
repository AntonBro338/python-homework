def chop (t) -> None:
    x = t.pop(0)
    x = t.pop(-1)
    return None

t = [1, 7, 30]
chop (t)
print (t)
