num = int(input('Введите новое число: '))
my_list = [7, 5, 4, 2, 1]
if num <= 1:
    my_list.append(num)
elif num == 2:
    my_list.insert(4, num)
elif num == 3:
    my_list.insert(3, num)
elif num == 4:
    my_list.insert(3, num)
elif num == 5:
    my_list.insert(2, num)
elif num == 6:
    my_list.insert(1, num)
elif num == 7:
    my_list.insert(1, num)
else:
    my_list.insert(0, num)
print(my_list)

