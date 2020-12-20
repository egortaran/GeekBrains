my_list = []


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


while True:
    el = input('Введите элемент: ')
    if el == "stop":
        break

    try:
        el = int(el)
    except ValueError:
        print("Вы ввели не число!")
    except OwnError as err:
        print(err)
    else:
        my_list.append(el)

print(my_list)
