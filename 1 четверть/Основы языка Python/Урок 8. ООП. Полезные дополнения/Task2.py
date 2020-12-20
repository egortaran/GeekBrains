class divZero:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        try:
            result = self.num1 / self.num2
        except ZeroDivisionError:
            print('Деление на 0')
        else:
            print(self.num1 / self.num2)


n=divZero(100, 3)
