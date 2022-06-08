import pandas as pd
import matplotlib.pyplot as plt
from tkinter import *  

def showDiagram(data, title, color, rotation, fontsize):
      plt.figure(figsize=(15, 5))
      plt.title(title)
      plt.plot(data.index, data.values, color = color)
      plt.grid(which='major', color = 'silver')
      plt.xticks(rotation = rotation, fontsize = fontsize)
      plt.show()

def firstTask(data):
      localDataFrame_1 = data.query('Rating > 3.1').groupby('Company Location')
      localDataFrame_2 = data.groupby('Company Location')
      localDataFrame = (localDataFrame_1['Rating'].count() / localDataFrame_2['Rating'].count()).dropna().sort_values(ascending=False)

      showDiagram(localDataFrame, 'Вероятность получения оценки выше 3.1 для каждой страны-производителя', 'r', 90, 6)

def secondTask(data):
      countries = ['Bolivia', 'Brazil', 'Canada', 'Colombia', 'Ecuador', 'U.S.A.']
      localDataFrame = data.groupby('Company Location')
      localDataFrame_1 = data.query('Rating > 3.1 and `Cocoa Percent` > 73').groupby('Company Location')['Rating'].count() / localDataFrame['Rating'].count()
      localDataFrame_2 = data.query('`Cocoa Percent` > 73').groupby('Company Location')['Rating'].count() / localDataFrame['Rating'].count()
      localDataFrame = (localDataFrame_1 / localDataFrame_2)[countries].sort_values(ascending=False)

      showDiagram(localDataFrame, 'Вероятность получения оценки выше 3.1 новым сортом какао с содержанием выше 73% из стран Северной и Южной Америк:', 'g', 0, 10)

def thirdTask(data):
      medianValue = data.query('`Review Date` > 2010')['Rating'].median()
      localDataFrame = data.query('`Review Date` > 2014').query(f'Rating > {medianValue}')['Rating'].count() / data.query('`Review Date` > 2014')['Rating'].count()
      window = Tk()  
      text="\n Прогнозируемая вероятность того, что обзоры после 2014 года \n будут иметь оценку выше медианной по всему периоду 2010 года: \n" + str(localDataFrame) + "%\n"
      lbl = Label(window, text = text, font = 50)  
      lbl.grid(column=0, row=0)  
      window.mainloop()

dataFrame = pd.read_csv('flavors_of_cacao.csv', header=0)
dataFrame['Cocoa Percent'] = dataFrame['Cocoa Percent'].replace('%', '', regex=True).astype('float64')

firstTask(dataFrame)
secondTask(dataFrame)
thirdTask(dataFrame)