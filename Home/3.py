def my_func(a, b, c):
    if a >= c and b >= c:
        return a + b
    elif a > b and a < c:
        return a + c
    else:
        return b + c
print(my_func(int(input("Введите число 1: ")), int(input("Введите число 2: ")), int(input("Введите число 3: "))))
