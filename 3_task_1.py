#  Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать
#  у пользователя, предусмотреть обработку ситуации деления на ноль.

def div(a, b):
    """a делится на b"""
    return a / b

a = int(input('Введите делимое - '))
b = int(input('Введите делитель - '))

if b == 0:
    print('На 0 делить нельзя!!!')
    b = int(input('Введите новый делитель отличный от 0 - '))
    print((div(a, b)))

else:
    print((div(a, b)))