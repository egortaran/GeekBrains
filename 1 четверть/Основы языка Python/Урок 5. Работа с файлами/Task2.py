with open("Task2_file.txt", "r") as f_obj:
    calc = 1
    my_str = f_obj.readlines()
    for word in my_str[0].split(" "):
        print(calc, " слово \"" + word + "\" ", len(word), " букв")
        calc += 1
    print("Итого ", calc - 1, "слов")
