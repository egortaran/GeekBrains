seasons = ['Зима', 'Весна', 'Лето', 'Осень']
months = ['Декабрь', 'Январь', 'Февраль',
          'Март', 'Апрель', 'Май',
          'Июнь', 'Июль', 'Август',
          'Сентябрь', 'Октябрь', 'Ноябрь']

myDict = {}
i = 0

# Ключ = месяц, Значение = время года
for season in seasons:
    for month in months[i:i + 3]:
        calendar = dict([[month, season]])
        myDict.update(calendar)
    i += 3

# Перемещает Декабрь в конец списка
months += [months.pop(0)]

number = int(input("Введите месяц в виде целого числа от 1 до 12: "))
userMonths = months[number-1]
print(f"Вы выбрали {userMonths} - {myDict.get(userMonths)}")
