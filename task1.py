# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n-1) + fib(n - 2)

# list_1 = []
# for i in range(1, 10):
#     list_1.append(fib(i))
# print(list_1)

# Задача 26
# def expon(a, b):
#     if b == 0:
#         return 1
#     return a * expon(a, b - 1)

# try:
#     a = int(input("Введите множимое основание: "))
#     b = int(input("Введите множитель: "))
# except ValueError:
#     print("Формат ввода не соответствует")
# else:
#     print(expon(a, b))

#  Задача 28
# def sum_digit(a, b):
#     if b == 0:
#         return a
#     return sum_digit(a + 1, b - 1)

# try:
#     a = int(input("Введите первое число: "))
#     b = int(input("Введите второе число: "))
# except ValueError:
#     print("Формат ввода не соответствует")
# else:
#     print(sum_digit(a, b))

#  Задача 2
# def amdiff(n):
#     if n == 0:
#         return b, c
#     elif 
#         n = n % 10

# try:
#     a = int(input("Введите первое число: "))
# except ValueError:
#     print("Формат ввода не соответствует")
# else:
#     print(amdiff(n))

def guess(n, m):
    if m == 0:
        print(f"Угадать не получилось. Загадано {n}")
        return n
    else:
        y = int(input("Введите случайное число от 0 до 100: "))
        if n == y:
            print(f"Вы отгадали. Загаданное число {y}")
        elif n > y:
            print("больше")
            guess(n, m - 1)
        else:
            n < y
            print("меньше")
            guess(n, m - 1)


try:
    a = int(input("Введите случайное число: "))
except ValueError:
    print("Формат ввода не соответствует")
else:
    z = guess(a, 3)
    