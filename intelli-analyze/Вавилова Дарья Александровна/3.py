#Метод половинного деления

import math

def half_interval(a, b):
    return (a + b) / 2

def get_parametr():
    a = int(input("Введите координату a : "))
    b = int(input("Введите координату b : "))
    E = float(input("Введите точность E: "))

    print('a = {a} Тип:{a1}\nb = {b} Тип {b1}\nE = {E} Тип:{E1}'
      .format(a=a, a1=type(a), b=b, b1=type(b), E=E, E1=type(E)))
    return a, b, E

def func(x):            
    return (2 - x) * math.exp(x)


def start():   
    a, b, E = get_parametr()
    counter = 0
    max_counter = 200

    while abs(b - a) > E:

        counter += 1
        if counter >= max_counter:
            print('Слишком много шагов')
            break

        if abs(b - a) <= E:
            print('Значение math.abs(b-a) стало меньше чем E')
            break

        print('\n\nШаг №{counter}'.format(counter=counter))
        #na - новая координата а
        #nb - новая координата b
        #nc - вычисленная функция на данном интервале
        na = func(a)
        c = half_interval(a, b)
        nc = func(c)
        if na * nc >= 0:
            a = c
        else:
            b = c
        print('na = {n_a} nc = {n_c} na * nc = {res}'.format(n_a=na, n_c=nc, res=na * nc))
        print('a = {a} b = {b}'.format(a=a, b=b))

start()
