#1. Функция с параметрами по умолчанию:
def print_params(a=1, b='строка', c=True):
    print(a, b, c)

# print_params(9, True, False, 'string', 0)
print_params(3, 9, 5)
print_params()
print_params(b = 25)
print_params(c = [1,2,3])


#2. Распаковка параметров:
values_list = [5, 'string', False]
values_dict = {'a' : 2, 'b' : 'integer', 'c' : False}

print_params(*values_list)
print_params(**values_dict)

#3. Распаковка + отдельные параметры:
values_list_2 = [7, 'dog']
print_params(*values_list_2, 42)