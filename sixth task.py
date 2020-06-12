name_1 = input('Введите название товара: ')
price_1 = input('Введите цену товара: ')
quantity_1 = input('Введите количество товара: ')
quantity_measure_1 = input('Введите единицу измерения товара: ')
list_1 = ['Название:', name_1, 'Цена:', price_1, 'Количество:', quantity_1, 'Единица измерения:', quantity_measure_1]
name_2 = input('Введите название товара: ')
price_2 = input('Введите цену товара: ')
quantity_2 = input('Введите количество товара: ')
quantity_measure_2 = input('Введите единицу измерения товара: ')
list_2 = ['Название:', name_2, 'Цена:', price_2, 'Количество:', quantity_2, 'Единица измерения:', quantity_measure_2]
name_3 = input('Введите название товара: ')
price_3 = input('Введите цену товара: ')
quantity_3 = input('Введите количество товара: ')
quantity_measure_3 = input('Введите единицу измерения товара: ')
list_3 = ['Название:', name_3, 'Цена:', price_3, 'Количество:', quantity_3, 'Единица измерения:', quantity_measure_3]
print(tuple(list_1))
print(tuple(list_2))
print(tuple(list_3))
analytics = input('Показать аналитику? да/нет: ')
if analytics == 'да':
    dict_name = ['Название: ', list_1[1], list_2[1], list_3[1]]
    dict_price = ['Цена: ', list_1[3], list_2[3], list_3[3]]
    dict_quantity = ['Количество: ', list_1[5], list_2[5], list_3[5]]
    dict_quantity_measure = ['Единица измерения товара: ', list_1[7], list_2[7], list_3[7]]
    print(dict_name)
    print(dict_price)
    print(dict_quantity)
    print(dict_quantity_measure)
else: none