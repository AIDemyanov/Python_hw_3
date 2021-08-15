# Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших
# двух аргументов

def my_func(a, b, c):
    if a >= b and b <= c:
        print(a + c)
    elif a <= b and a >= c:
        print(a + b)
    else:
        print(b + c)


my_func(1, 2, 3)