def nested_sum(t):
 return sum(sum(_list_) for _list_ in t)

t = [[1, 2], [3], [4, 5, 6]]

print(nested_sum(t))
