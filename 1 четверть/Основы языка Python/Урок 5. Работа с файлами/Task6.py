amount = 0
lessons = {}

with open("Task6_file.txt", "r", encoding='utf-8') as f_obj:
    for line in f_obj:
        line = line.split(':')
        name = str(line[0])
        for num1 in line[1].split(" "):
            counter = 0
            for i in reversed(num1):
                if i.isdigit():
                    amount += int(i) * 10**counter
                    counter += 1
        lessons.update({name: amount})
        amount = 0
print(lessons)
