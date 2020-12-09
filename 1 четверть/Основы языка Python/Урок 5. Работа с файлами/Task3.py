with open("Task3_file.txt", "r") as f_obj:
    my_str = f_obj.readlines()
    my_str = my_str[0].split(", ")
    calk1 = 0
    calk2 = 0
    for salary in my_str:
        word = salary.split(" ")
        calk1 += 1
        calk2 += int(word[1])
        if int(word[1]) <= 20000:
            print(word[0])
    print("Средний доход = ", calk2 / calk1)
