def my_func(num1, num2, num3):
    if num1 + num2 > num2 + num3 and num1 + num2 > num1 + num3:
        print(num1 + num2)
    elif num2 + num3 > num1 + num3:
        print(num2 + num3)
    else:
        print(num1 + num3)


my_func(int(input("1 Число: ")), int(input("2 Число: ")), int(input("3 Число: ")))
