from random import *


my_list = [randint(0, 25) for i in range(20)]
new_list = [i for i in my_list if my_list.count(i) == 1]
print(my_list)
print(new_list)
