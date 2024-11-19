def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(a = 8, c = False)
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [1, 'один', True]
values_dict = { 'a': 0, 'b': 'ноль', 'c': False}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['2', 2]
print_params(*values_list_2, 42)