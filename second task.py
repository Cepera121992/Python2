
my_list = [input('Введите любое слово: '), input('Введите любое целое число: '), input('Введите любое число: '), input('Введите True or False: ')]
a = my_list[0]
my_list[0] = my_list[1]
my_list[1] = a
b = my_list[2]
my_list[2] = my_list[3]
my_list[3] = b
print (my_list)