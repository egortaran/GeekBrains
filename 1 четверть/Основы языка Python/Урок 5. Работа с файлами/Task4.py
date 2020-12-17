counter = 0

with open("Task4_1_file.txt", "r") as f_obj:
    newFile = open("Task4_2_file.txt", "w")
    for line in f_obj:
        counter += 1
        line_content = line.split('-')
        if counter == 1:
            line_content[0] = 'Один'
        elif counter == 2:
            line_content[0] = 'Два'
        elif counter == 3:
            line_content[0] = 'Три'
        else:
            line_content[0] = 'Четыре'
        newFile.write(line_content[0] + ' - ' + str(counter) + '\n')

    newFile.close()