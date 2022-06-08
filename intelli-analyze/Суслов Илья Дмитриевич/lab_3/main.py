#Импортируем модули и настроим среду
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display, Latex
from types import FunctionType
from functools import partial

plt.rcParams['figure.figsize'] = 8, 6

# Задание. Реализовать в функциональной парадигме приближенное вычисление корней уравнения f(x) с заданной (с клавиатуры при запуске) точностью e
eps = float(input('Введите e: '))

def dy(x, fn, n=1):
	h = 1e-5
	
	match n:
		case 1:
			return round((fn(x+h) - fn(x-h)) / (2*h), 5)
		case 2:
			return round((fn(x+h) - 2*fn(x) + fn(x-h)) / h**2, 5)
		case _:
			raise ValueError('No implementation for n is %s' % n)

# Реализуем функцию plot для визуализации графиков функций и их пересечений
def plot(fn, xx, yy, root, title, show_axes=True):
  plt.xlabel('$x$')
  plt.ylabel('$y$')
  plt.title(title)
  plt.plot(xx, yy, c='blue', label='$f(x)$')


  if type(fn) is FunctionType:
    plt.plot(xx, fn(xx), c='orange', label='$g(x)$')
    plt.plot(root, fn(root), 'ro')
  else:
    plt.axhline(fn, c='orange', label='$g(x)$')
    plt.plot(root, 0, 'ro')
    
  if show_axes:
    plt.axvline(x=0, c="gray", label="$x=0$", linewidth=0.5)
    plt.axhline(y=0, c="gray", label="$y=0$", linewidth=0.5)
	
  plt.legend()
  plt.show()

# x^2 = ln(x + 1) методом простых итераций
def find_c(x1, x2, f):
  extrema = dy(x1, f), dy(x2, f)
  return 2/(np.max(extrema) + np.min(extrema))

# Возьмём интервалы (-0.5; 0.5) для первого корня и (0.5; 1) для второго соответственно
f = lambda x: np.log(x + 1) - x**2
phi = lambda x, c: x - c*(np.log(x + 1) - x**2)
g = lambda x: x

c = find_c(-0.5, 0.5, f)


def find_root(x, c):
  phi_ = partial(phi, c=c)
  return find_root(phi_(x), c) if np.abs(x - phi(x, c)) >= eps else x


title = 'Пересечение функций $\phi(x)=x-c(ln(x + 1)-x^2)$ и $g(x)=x$'
xx = np.linspace(-0.5, 2, 100)
root = find_root(-0.5, c)

print(f'Корень f(x) на интервале (-0.5, 0.5) равен {root.round(3)}')
plot(g, xx, phi(xx, c), root, title)

c = find_c(0.5, 1, f)
root = find_root(1, c)

print(f'Корень f(x) на интервале (0.5, 1) равен {root.round(3)}')
plot(g, xx, phi(xx, c), root, title)