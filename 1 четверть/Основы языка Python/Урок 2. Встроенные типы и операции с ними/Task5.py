my_list = [7, 5, 3, 3, 2]
while True:
    num = int(input("Введите число: "))
    my_list.append(num)
    i = len(my_list) - 1
    while True and i != 0:
        if my_list[i] > my_list[i-1] or my_list[i] == my_list[i-1]:
            my_list[i], my_list[i-1] = my_list[i-1], my_list[i]
        else:
            break
        i -= 1
    print(my_list)
