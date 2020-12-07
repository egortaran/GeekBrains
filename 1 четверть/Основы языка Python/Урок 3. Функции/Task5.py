def resultSum(it):
    total = 0
    for i in it:
        if i == "q":
            return total
        total += int(i)
    return total


sum1 = 0
while True:
    result = list(input("Строка чисел: ").split(" "))
    sum1 += resultSum(result)
    print(f"Результат: {sum1}")

    if "q" in result:
        break
