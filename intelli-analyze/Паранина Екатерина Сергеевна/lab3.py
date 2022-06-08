import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return np.log10(1+2*x)-2+x


def bn1(a, b):
    return b-((a-b)/(f(a)-f(b)))*f(b)


def koren(a, b, e):
    if(abs(b-bn1(a, b)) < e):
        return bn1(a, b)
    else:
        return koren(a, bn1(a, b), e)


print('Вариант', len('Паранина Екатерина Сергеевна') % 5)
print('Метод хорд')
print('lg(1+2x)=2-x')


x = np.linspace(-0.4, 10, 1000)
plt.subplot()
plt.plot(x, f(x))
plt.xlabel("x")
plt.ylabel("f(x)")
plt.axhline(0, color='black', linestyle='--')
plt.show()


a = 0
b = 2
print('a=',a,'b=',b)
e = float(input('Введите точность e='))

print('x=',koren(a, b, e))
