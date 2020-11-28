list_1 = []
i = 1
while True:
    element = input(f'Для заполнение списка введите break\nВведите {i} элемент: ')
    if element == "break":
        break
    list_1.append(element)
    print(f"\n\nСписок элементов: {list_1}")
    i += 1

length = len(list_1)
if length % 2 == 1:
    length -= 1

for el in range(0, length, 2):
    list_1[el], list_1[el+1] = list_1[el+1], list_1[el]

print(f"\n\nРезультат: {list_1}")
