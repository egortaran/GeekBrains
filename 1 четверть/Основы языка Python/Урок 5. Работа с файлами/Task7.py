total_profit = 0
company_dict = {}
counter = 0

with open("Task7_1_file.txt", "r", encoding='utf-8') as f_obj:
    for line in f_obj:
        counter += 1
        company_info = line.split(' ')
        company_name = str(company_info[1])
        income = int((company_info[2]))
        losses = int((company_info[3]))
        profit = income - losses
        total_profit += profit
        profit_to_loss = (profit/losses)
        result = f"Прибыль {profit}, Отношение прибыли к убыткам {'{:.2f}'.format(profit_to_loss)}"
        company_dict.update({company_name: result})

average_dict = {'Средняя прибыль': total_profit/counter}
with open("Task7_2_file.txt", "w", encoding='utf-8') as f_obj:
    f_obj.write(str(company_dict))
    f_obj.write(str(average_dict))
