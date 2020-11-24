a = int(input("Введите параметр а: "))
b = int(input("Введите параметр b: "))
day = 1

print("\nРезультат:\n")

print(f"{day}-й день: {a} км")

while a <= b:
    a = float('{:.2f}'.format(a * 1.1))
    day += 1
    print(f"{day}-й день: {a} км")
print(f"\nНа {day}-й день спортсмен достиг результата — не менее {b} км.")
