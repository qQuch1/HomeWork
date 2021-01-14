from sys import argv

name, time, salary, bonus = argv #Почему не работает? Объясните пожалуйста )

try:
    time = int(time)
    salary = int(salary)
    bonus = int(bonus)
    res = time * salary + bonus
    print(f'Зарплата сотрудника: {res}')
except ValueError:
    print('Not a number')
