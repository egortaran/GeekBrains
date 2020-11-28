strUser = input("Введите строку их нескольких слов, разделённых пробелами: ")
listUser = strUser.split()

i = 0
for i in range(len(listUser)):
    print(f"{i+1}. {listUser[i][:10]}")
