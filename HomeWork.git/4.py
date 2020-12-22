number = input("Введите число: ")
a = 0
for i in number:
    while int(i) > a:
        a = int(i)
print(f"Наибольшая цифра в числе: {a}")


