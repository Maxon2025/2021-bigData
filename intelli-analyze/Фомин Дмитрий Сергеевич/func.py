import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np


print("Var " + str(len('Фомин Дмитрий Сергеевич') % 5))

x = np.arange(-6, 5.01, 0.01)
plt.plot(x, np.log10(1+2*x)-2+x)
plt.plot(x,x*0,color = 'orange',linestyle = '--',)
plt.plot(x*0,x,color = 'orange',linestyle = '--',)
plt.show()

a = 0
b = 2
def F(x):
    return np.log10(1+2*x)-2+x
def C(a,b):
    return a - F(a)*(a-b)/(F(a)-F(b))
def eps(a,b):
    return abs(a-C(a,b))
    
def sol(precision,a,b):   
    if eps(a,b)>precision:       
        if F(a)*F(C(a,b))<=0:
            return sol(precision,a,C(a,b))
        else:
            return sol(precision,C(a,b),b)
    else:
        return a

print("\nEquation: lg(1+2*x)=2-x")
precision = float(input("Type what presition do you need?\n"))
print("x="+str(sol(precision,a,b)))
