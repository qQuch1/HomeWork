text = input("Введите строку: ")
a = text.split(" ")
for i, num in enumerate(a, 1):
    if len(num) > 10:
        num = num[0:10]
    print(f"{i} - {num}")
