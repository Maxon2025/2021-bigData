import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('flavors_of_cacao.csv')
data['Cocoa Percent'] = data['Cocoa Percent'].replace('%', '', regex=True).astype('float32')
rating = data['Rating']

byRating = data.groupby('Broad Bean Origin')[['Broad Bean Origin', 'Rating']]
byCocoa = data.groupby('Cocoa Percent')['Rating']

index = list(byRating.groups.keys())

def plot(ax, plots, styles=['-', '-'], colors=['y', 'c']):
    for item, color, style in zip(plots.keys(), colors, styles):
        ax.plot(plots[item], label=item, linestyle=style, color=color)
    ax.legend()


def line(ax, values, colors=['r', '0']):
    for value, color in zip(values.keys(), colors):
        ax.axhline(values[value], label=value, color=color, linestyle=':', alpha=0.8)
    ax.legend()


def plot_contry():
    fig, ax = plt.subplots(2, 1, sharex=True, figsize=(16, 6))
    ax[1].xaxis.set_major_locator(plt.FixedLocator(index))
    ax[1].set_xticklabels(labels=index, rotation=90)

    plot(ax[0], {"Медиана": byRating.median(), "Среднее": byRating.mean()})
    line(ax[0], {"Общ. Медиана": rating.median(), 'Общ. Среднее': rating.mean()})

    plot(ax[1], {"Дисперсия": byRating.var().fillna(0), "СКО": byRating.std().fillna(0)}, colors=['purple', 'green'])
    line(ax[1], {"Общ. Дисперсия": rating.var(), 'Общ. СКО': rating.std()}, colors=['purple', 'green'])


def plot_cocoa():
    fig, ax = plt.subplots(2, 1, sharex=True, figsize=(16, 6))

    ax[1].xaxis.set_major_locator(plt.MaxNLocator(20))
    ax[1].xaxis.set_major_formatter(plt.FuncFormatter(lambda x, pos: f'{x}%'))

    plot(ax[0], {'Дисперсия для какао в процентках': byCocoa.var().fillna(0)}, styles=['-'])
    line(ax[0], {'Общ. Дисперсия': rating.var()})

    plot(ax[1], {'Размах для какао в процентках': (byCocoa.max() - byCocoa.min())}, colors=['c'], styles=['-'])
    line(ax[1], {'Общ. Размах': (rating.max() - rating.min())}, colors=['c'])

plot_contry()
plot_cocoa()

plt.show()