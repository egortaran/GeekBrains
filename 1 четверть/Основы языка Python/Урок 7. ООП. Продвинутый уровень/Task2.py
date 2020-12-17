from abc import ABC, abstractmethod


my_sum = 0


class Clothing(ABC):
    value: float

    @abstractmethod
    def fabric_consumption(self):
        return round(self.value, 2)


class Coat(Clothing):
    def __init__(self, value):
        global my_sum
        self.value = value / 6.5 + 0.5
        my_sum += super().fabric_consumption()

    def fabric_consumption(self):
        return super().fabric_consumption()


class Suit(Clothing):
    def __init__(self, value):
        global my_sum
        self.value = 2 * value + 0.3
        my_sum += super().fabric_consumption()

    def fabric_consumption(self):
        return super().fabric_consumption()


a = Coat(5)
b = Suit(6)
c = Coat(9)
print('a =', a.fabric_consumption())
print('b =', b.fabric_consumption())
print('c =', c.fabric_consumption())

print('my_sum = ', my_sum)
