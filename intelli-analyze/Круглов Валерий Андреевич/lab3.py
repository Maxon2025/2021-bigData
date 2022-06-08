import math
from tkinter import *
from unittest import result  
  
def createWindow():

      def clicked():
            try:
                  result = "x = " + str(solve(float(aTxt.get()), float(bTxt.get()), float(eTxt.get())))
                  resultLabel.configure(text = result)
            except ValueError:
                  resultLabel.configure(text = "Введено недопустимое значение.") 

      window = Tk()  
      window.title("Метод касательных")  
      window.geometry('535x135')
      window.resizable = False
      headerLabel = Label(window, text = "Программа найдёт приближенное значение x для уравнения\nlnx+(x+1)³=0")
      headerLabel.grid(column = 0, row = 0)
      boundarieslabel = Label(window, text = "Введите значения концов рассматриваемого отрезка ab:")
      boundarieslabel.grid(column = 0, row = 1)
      aLabel = Label(window, text = "a = ")
      aLabel.grid(column = 1, row = 1)
      aTxt = Entry(window,width=10)  
      aTxt.grid(column=2, row=1)
      bLabel = Label(window, text = "b = ")
      bLabel.grid(column = 3, row = 1)
      bTxt = Entry(window,width=10)  
      bTxt.grid(column=4, row=1) 
      eLabel = Label(window, text = "Введите погрешность:")
      eLabel.grid(column = 0, row = 2, sticky = 'W')
      eTxt = Entry(window,width=10)  
      eTxt.grid(column=0, row=2)

      button = Button(window, text="Вычислить", command = clicked)  
      button.grid(column=0, row=4)  

      resultLabel = Label(window, text ="")  
      resultLabel.grid(column = 0, row = 5)

      window.mainloop()

def function(x):
      return math.log(x) + math.pow((x + 1), 3)

def firstDerivative(x):
      return 3 * math.pow((x + 1), 2) + 1/x

def secondDerivative(x):
      return 6 * (x + 1) - 1/math.pow(x,2)

def checkBoundaries(a, b):
      if (a>0)and(function(a)*secondDerivative(a)>0):
            return a
      elif (b>0)and(function(b)*secondDerivative(b)>0):
            return b
      else:
            raise ValueError("Нельзя так делать.")

def findX(x, e):
      if (abs(function(x)/firstDerivative(x)) > e):
        return findX(x-function(x)/firstDerivative(x), e)
      else:
        return x

def solve(a, b, e):
            x = checkBoundaries(a, b)
            return findX(x, e)
            
createWindow()