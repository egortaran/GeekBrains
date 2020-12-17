with open("Task1_file.txt", "w") as f_obj:
    while True:
        str1 = input("Введите строку: ")
        if not str1:
            break
        f_obj.write(str1 + '\n')
