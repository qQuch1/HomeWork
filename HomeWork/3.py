season = {"Зима" : (1,2,12),
          "Весна" : (3,4,5),
          "Лето" : (6,7,8),
          "Осень" : (9,10,11)
          }
number = int(input("Введите номер месяца: "))
while number >= 13 or number <= 0:
    number = int(input("Введите номер месяца: "))

for key in season.keys():
    if number in season[key]:
        print(key)
