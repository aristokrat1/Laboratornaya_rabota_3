salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

# TODO Оформить решение
sum_spend = spend
sum_salary = salary
for i in range (2,months + 1):
    spend = spend + increase * spend
    sum_spend = sum_spend + spend
    sum_salary = sum_salary + salary
need_money = sum_spend - sum_salary
print(round(need_money))
