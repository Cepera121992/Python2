my_str = input('Введите любое предложение: ')
word = my_str.split()
for i, el in enumerate(word, 1):
    print(i, el[:10])
