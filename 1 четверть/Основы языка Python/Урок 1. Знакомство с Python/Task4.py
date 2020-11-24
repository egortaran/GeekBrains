num = int(input("Введите целое положительное число: "))

i = num
numMax = 0

while i != 0:
    if numMax < num % 10:
        numMax = num % 10
    num = int(num / 10)
    i = i/10 + (i/10) % 10
print(numMax)
