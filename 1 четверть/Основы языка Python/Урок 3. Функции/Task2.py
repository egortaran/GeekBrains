def userCreate(name, secondName, year,
               city, email, phone):
    print(f"{name} {secondName}, {year}г, г.{city}, email: {email}, тел. {phone}")


userCreate(input("Имя: "),
           input("Фамилия: "),
           int(input("Год: ")),
           input("Город: "),
           input("email: "),
           input("тел.: "))
