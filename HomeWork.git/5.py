income = int(input("Введите выручку фирмы: "))
spending = int(input("Введите издержки фирмы: "))
if income > spending:
    count = income - spending
    print(f"Выручка с учетом издержек составляет - {count} рублей.")
    employee = int(input("Введите количество сотрудников: "))
    count2 = count / employee
    print(f"Зарплата одного сотрудника состовляет - {count2} рублей.")
elif income == spending:
    print("Фирма работает в 0.")
else:
    print("Фирма работает в минус.")



