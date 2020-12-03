def split(num1, num2):
    try:
        print(f"{num1} / {num2} = {(num1 / num2):.2f}")
    except ZeroDivisionError:
        print("На 0 делить нельзя")


split(int(input("Первое число: ")), int(input("Второе число: ")))
