class OrganicCell:
    def __init__(self, value: int):
        self.value = value

    def __add__(self, other):
        return OrganicCell(self.value + other.value)

    def __sub__(self, other):
        my_sum = self.value - other.value
        if my_sum > 0:
            return OrganicCell(my_sum)

    def __mul__(self, other):
        return OrganicCell(self.value * other.value)

    def __truediv__(self, other):
        return OrganicCell(int(round(self.value / other.value, 0)))

    def __str__(self):
        return f"{self.value}"

    def make_order(self, div):
        my_str = ''
        stars = self.value
        i = 0

        while stars:
            my_str += '*'
            stars -= 1
            i += 1
            if i == div:
                my_str += '\n'
                i = 0
        return my_str


a = OrganicCell(27)
b = OrganicCell(13)
print('a+b =', a + b)
print('a-b =', a - b)
print('a*b =', a * b)
print('a/b =', a / b)

print('Организация ячейки a по рядам\n' + a.make_order(5))
