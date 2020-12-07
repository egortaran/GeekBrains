from __future__ import print_function


def int_func(newWord):
    return newWord.capitalize()


for word in input("Ввод: ").split(" "):
    print(int_func(word).rstrip('n'), end=' ')
