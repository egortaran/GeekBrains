proceeds = int(input("Введите выручку: "))
cost = int(input("Введите издержки: "))

if proceeds > cost:
    print("Выручка больше издержек")
    print(f"Рентабельность выручки = {int(proceeds / cost * 100)}%")
    workers = int(input("\nЧисленность сотрудников фирмы: "))
    print(f"Прибыль фирмы в расчете на одного сотрудника = {float('{:.1f}'.format((proceeds - cost) / workers))}")
elif proceeds == cost:
    print("Выручка равна издержкам\n")
else:
    print("Выручка меньше издержек\n")
