# Неполучившиеся решение. Напишите, пожалуйста, в комментариях, почему когда я ввожу 5, он мне говорит, что это зима?
# month = int(input('Введите числовое значение месяца: '))
# winter = [12, 1, 2]
# spring = [3, 4, 5]
# summer = [6, 7, 8]
# autumn = [9, 10, 11]
# if month == winter[0] or winter[1] or winter[2]:
#     print ('Это зима!')
# elif month == spring[0] or spring[1] or spring[2]:
#     print ('Это весна!')
# elif month == summer[0] or summer[1] or summer[2]:
#     print ('Это лето!')
# elif month == autumn[0] or autumn[1] or autumn[2]:
#     print ('Это осень!')
# else:
#     print('Такого месяца не существует!')

# Решение через list:
# month = int(input('Введите числовое значение месяца: '))
# seasons = ['Это зима!', 'Это весна!', 'Это лето!', 'Это осень!']
# if month  == 12 or month == 1 or month == 2:
#     print(seasons[0])
# elif month == 3 or month == 4 or month == 5:
#     print(seasons[1])
# elif month == 6 or month == 7 or month == 8:
#     print(seasons[2])
# elif month == 9 or month == 10 or month == 11:
#     print(seasons[3])
# else:
#     print('Такого месяца не существует!')

# Решение через dict
month = int(input('Введите числовое значение месяца: '))
seasons = {1: 'Это зима!', 2: 'Это весна!', 3: 'Это лето!', 4: 'Это осень!'}
if month  == 12 or month == 1 or month == 2:
    print(seasons[1])
elif month == 3 or month == 4 or month == 5:
    print(seasons[2])
elif month == 6 or month == 7 or month == 8:
    print(seasons[3])
elif month == 9 or month == 10 or month == 11:
    print(seasons[4])
else:
    print('Такого месяца не существует!')