money_capital = 6000
salary = 5000
spend = 6000
increase = 0.05
# изначальное значение money_capital - 10000, но с ним число месяцев получается 5
month = 0  # количество месяцев, которое можно прожить
while money_capital + salary > spend:

    money_capital = money_capital + salary
    spend = spend + increase * spend
    money_capital = money_capital - spend
    month = month + 1

# TODO Оформить решение

print(month)
