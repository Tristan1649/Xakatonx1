name_p = []
size_p = 1000

while True:
    name_predmet = input('Введите название предмета >>> ')
    size_predmet = int(input('Введите размер предмета >>> '))

    name_p.append(name_predmet)

    if name_predmet is None:
        print('Введи название предмета')
    if size_predmet is None:
        print('Введи размер предмета')

    size_p -= size_predmet

    if size_p < 0:
        print('Места в полке заполнено')
    print(name_p,size_p)
