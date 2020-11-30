items = []

while True:
    name = input("Введите название: ")
    price = int(input("Введите цену: "))
    amount = int(input("Введите количество: "))
    unit = input("Введите единицу измерения: ")

    toDict = {"Название": name, "цена": price,
              "количество": amount, "eд": unit}
    toList = (len(items)+1, toDict)
    items.append(toList)

    for i in range(0, len(items)):
        print(items[i])

    goNext = input("\nСтруктура готова? (да/любое значение)\n")
    if goNext == "да":
        break

nameList = []
priceList = []
amountList = []
unitList = set()

for item in items:
    nameList.append(item[1].get("Название"))
    priceList.append(item[1].get("цена"))
    amountList.append(item[1].get("количество"))
    unitList.add(item[1].get("eд"))

analytics = {"Название": nameList, "цена": priceList,
             "количество": amountList, "eд": unitList}

print("\nАналитика о товарах:\n")

for title in analytics.keys():
    print(title, ": ", analytics[title])

