def my_func(x, y):
    num = 1
    for i in range(abs(y)):
        num *= x
    if y >= 0:
        print(f"Результат:  {num}")
    else:
        print(f"Результат:  {1 / num}")


x = float(input("Действительное положительное число x: "))
y = int(input("Целое отрицательное число y: "))

if x >= 0 and y < 0:
    my_func(x, y)
else:
    print("Вы что-то ввели неправильно")
