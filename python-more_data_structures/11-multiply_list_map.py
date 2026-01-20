def multiply_list_map(my_list=[], number=0):
    mul = lambda num: num * number
    return list(map(mul, my_list))
