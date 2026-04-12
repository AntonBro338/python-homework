def is_sorted(t) :
    for i in range(len(t) - 1):
        if t[i] > t[i + 1]:
            return False
    return True

t = [1, 2, 3, 4, 5, 6]
print (is_sorted (t))
