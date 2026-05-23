

def biggest_dict(**kwargs) -> dict[str, str | int]:
    my_dict = {}
    my_dict.update(**kwargs)
    return my_dict


print (biggest_dict(k1=22, k2=31, k3=11, k4=91))
print (biggest_dict(name='Елена', age=31, weight=61, eyes_color='grey'))
