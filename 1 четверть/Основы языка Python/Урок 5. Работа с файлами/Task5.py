from random import *


counter = 0
numbers = [randint(0, 100) for i in range(10)]
with open("Task5_file.txt", "w") as f_obj:
    for num in numbers:
        f_obj.write(str(num) + " ")
        counter += num
    print(counter)
