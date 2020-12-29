def my_sum ():
    sum = 0
    whl = False
    while whl == False:
        number = input("Что-бы завершить программу нажимте Q\nВведите число: ").split()
        result = 0
        for i in range(len(number)):
            if number[i] == 'q' or number[i] == 'Q':
                whl = True
                break
            else:
                result = result + int(number[i])
        sum += result
        print(f"Сумма чисел: {sum}")
    print(f'Общая сумма: {sum}')
my_sum()
