wage = 15000
bonus = 10000
income = {"wage": wage, "bonus": bonus}


class Worker:
    def __init__(self, name, surname, position, _income=None):
        if _income is None:
            _income = {}
        self.name = name
        self.surname = surname
        self.position = position
        self._income = _income


class Position(Worker):
    def get_full_name(self):
        print(f"Полное имя сотрудника {self.name} {self.surname}")

    def get_total_income(self):
        print(f"Доход с учетом премии {sum(self._income.values())}")


a = Position("Егор", "Таран", "Директор", income)
a.get_full_name()
a.get_total_income()
