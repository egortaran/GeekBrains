class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list

    def __str__(self):
        n1 = '\n'
        return f"Матрица: \n{n1.join([str(el) for el in self.my_list])}"

    def __add__(self, other):
        matrix1 = self.my_list
        matrix2 = other.my_list

        result = []
        for sublist in zip(matrix1, matrix2):
            temp = []
            for numbers in zip(sublist[0], sublist[1]):
                temp.append(sum(numbers))
            result.append(temp)
        return Matrix(result)


a = Matrix([[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]])

b = Matrix([[2, 3, 1],
            [9, 7, 6],
            [5, 4, 0]])

print(a, '\n')
print(a+b)
