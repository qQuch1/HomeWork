def my_func(a, b):
    try:
        x = a / b
        return x
    except ZeroDivisionError:
        return "Нельзя использовать 0 в качестве деления!"
print(my_func(int(input("Введите первое число: ")), int(input("Введите второе число: "))))
