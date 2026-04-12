def middle(t): 
    if len(t) <= 2:
        return []
    else:
        return t[1:-1]

t = [1, 2, 3, 4]
print (middle(t))
