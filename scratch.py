import math
print('Введите коэффициента для уравнения ax**2 + bx + c = 0 ')
a = float(input("a = "))
b = float(input('b = '))
c = float(input("c = "))
diskr = b ** 2 - 4 * a * c
print(f'{a}x**2 + {b}x + c = 0')
print('Дискриминант равен - ', diskr)
if diskr < 0:
    print('У данного уравнения корней нет')
if diskr >= 0:
    x1 = (-b + math.sqrt(diskr)) / (2 * a)
    x2 = (-b - math.sqrt(diskr)) / (2 * a)

    if x1 == x2:
        print('Корни равны, x = ', x1)
    else:
        print('Первый корень равен - ', x1)
        print('Второй корень равен - ', x2)





