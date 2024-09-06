def print_params(a=1, b='строка', c=True):
    print(a, b, c)


values_list = [False, [12], 12]
values_dict = {'a': 'a', 'b': 2, 'c': True}
values_list_2 = [54.32, 'Строка']

print_params(b=25)
print_params(c=[1, 2, 3])
print()
print_params(*values_list)
print_params(**values_dict)
print()
print_params(*values_list_2, 42)
