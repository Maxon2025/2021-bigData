import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('flavors_of_cacao.csv')
data['Cocoa Percent'] = data['Cocoa Percent'].replace('%', '', regex=True).astype('float32')
rating = data['Rating']

groupedByRating = data[['Company Location', 'Rating']]
groupedByRating = groupedByRating.groupby('Company Location')[['Company Location', 'Rating']]

def plot(ax, plots, styles=['-', '-'], colors=['g', 'r']):
    for item, color, style in zip(plots.keys(), colors, styles):
        ax.plot(plots[item], label=item, linestyle=style, color=color)
    ax.legend()

def company():
    plt.figure(figsize=(16, 7))
    plt.subplots_adjust(hspace=0.1)
    сolumn = groupedByRating.groups.keys()
    array = np.empty(len(groupedByRating.groups.values()))

    array[...] = rating.var()
    plt.subplot(2, 1, 1)
    plt.plot(сolumn, groupedByRating.var().fillna(0)['Rating'], label='Дисперсия Rating', color='g')
    plt.plot(сolumn, array, "--", label='Общая дисперсия', color='yellowgreen')
    
    array[...] = rating.std()
    plt.plot(сolumn, groupedByRating.std().fillna(0)['Rating'], label='СКО Rating', color='r')
    plt.plot(сolumn, array, "--", label='Общее СКО', color='lightcoral')
    plt.xticks(color='w')

    plt.grid(which='major', color = 'silver')
    plt.legend(fontsize=10)

    array[...] = rating.mean()
    plt.subplot(2, 1, 2)
    plt.plot(сolumn, groupedByRating.mean()['Rating'], label='Среднее Rating', color='g')
    plt.plot(сolumn, array, "--", label='Общее среднее', color='yellowgreen')
    
    array[...] = rating.median()
    plt.plot(сolumn, groupedByRating.median()['Rating'], label='Медианное Rating', color='r')
    plt.plot(сolumn, array,"--", label='Общее Медианное', color='lightcoral')
    
    plt.grid(which='major', color = 'silver')
    plt.xticks(rotation =  90, fontsize = 6)
    plt.legend(fontsize = 10)

def cocoa():
    cocoaX = data.sort_values(by='Cocoa Percent')['Cocoa Percent'].unique()
    cocoaX = cocoaX.astype(float)
    cocoaX = np.sort(cocoaX)
    cocoaX = cocoaX.astype(str)
    cocoaX = [i.replace('.0', '') for i in cocoaX]
    cocoaY = data.groupby('Cocoa Percent')['Rating']

    plt.figure(figsize=(16, 7))
    plt.subplots_adjust(hspace=0.1)
    array = np.empty(len(cocoaX))
    
    array[...] = cocoaY.var().fillna(0)
    plt.subplot(2, 1, 1)
    plt.plot(cocoaX, array, label='Дисперсия', color='g')
    array[...] = rating.var()
    plt.plot(cocoaX, array, "--", label='Общая дисперсия', color='yellowgreen')
    
    plt.xticks(color='w')
    plt.grid(which='major', color = 'silver')
    plt.legend(fontsize=10)

    array[...] = cocoaY.max() - cocoaY.min()
    plt.subplot(2, 1, 2)
    plt.plot(cocoaX, array, label='Размах', color='r')
    array[...] = rating.max() - rating.min()
    plt.plot(cocoaX, array, "--", label='Общий размах', color='lightcoral')
    
    plt.xticks(rotation =  90)
    plt.grid(which='major', color = 'silver')
    plt.legend(fontsize=10)

cocoa()
company()

plt.show()