import numpy as np

# Tangent method or Newton 's method
# log(x)+((x+1)**3) = 0
# derivative: (1/x)+(3*((x+1)**(2)))

def newton(f,Df,x0,epsilon,max_iter):
    xn = x0
    for n in range(0,max_iter):
        fxn = f(xn)
        if abs(fxn) < epsilon:
            print('Found solution after', n, 'iterations')
            return xn
        Dfxn = Df(xn)
        if Dfxn == 0:
            print('No solution found')
            return None
        xn = xn - fxn/Dfxn
    print('Exceeded maximum iterations. No solution found')
    return None

var=len('Жирнова Полина Михайловна')%5
print("\nВариант", var)
print("\nМетод касательных")
print("\nФункция: ln x + (x+1)^3 = 0")

x = float(input("\nВведите начальное значение х0: "))
presition = float(input("\nВведите погрешность: "))

p = lambda x: np.log(x)+((x+1)**3)
Dp = lambda x: (1/x)+(3*((x+1)**(2)))

print("x = ", newton(p,Dp,x,presition,1000))
