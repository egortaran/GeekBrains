class Data:
    def __init__(self, my_str: str):
        new_str = my_str.split("-")
        self.my_str = [int(it) for it in new_str]

    def go(self):
        print(self.my_str)

    @classmethod
    def take(cls, my_str: str):
        if cls.check(my_str):
            new_str = my_str.split("-")
            day = int(new_str[0])
            month = int(new_str[1])
            year = int(new_str[2])
            print("День ", day, ". Месяц ", month, ". Год", year)

    @staticmethod
    def check(my_str: str):
        new_str = my_str.split("-")
        try:
            new_str = [int(it) for it in new_str]
            if 31 < new_str[0] < 0 and 0 < new_str[1] <= 12:
                print("Введите коректное значение")
                return False
            return True
        except ValueError:
            print("Введите коректное значение")


user_data = "13-9-2020"
Data.take(user_data)
