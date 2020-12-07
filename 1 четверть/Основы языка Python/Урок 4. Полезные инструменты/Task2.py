from random import *


my_list = []
new_list = []

for i in range(10):
    my_list.append(randint(0, 20))
print(my_list)

for i in range(1, 10):
    if my_list[i] > my_list[i-1]:
        new_list.append(my_list[i])
print(new_list)
