import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def plot(ax, data, funcs, names):
    for i in range(len(ax)):
        ax[i].plot(funcs[i](data).fillna(0))
        ax[i].axhline(funcs[i](rating), linestyle=":")
        ax[i].set_title(names[i])


def first():
    fig, ax = plt.subplots(2, 2, sharex=True, figsize=(16, 6))

    funcs = [lambda x: x.median(), lambda x: x.mean(), lambda x: x.var(), lambda x: x.std()]
    names = ["Медиана", "Среднее", "Дисперсия", "СТО"]

    plot(np.concatenate(ax).flat, byDate, funcs, names)
    plt.show()


def second():
    fig, ax = plt.subplots(2, 1, sharex=True, figsize=(16, 6))

    funcs = [lambda x: x.var(), lambda x: x.max() - x.min()]
    names = ["Дисперсия", "Размах"]

    plot(ax, byCocoa, funcs, names)
    plt.show()


data = pd.read_csv('flavors_of_cacao.csv')
data['Cocoa Percent'] = data['Cocoa Percent'].replace('%', '', regex=True).astype('float32')

rating = data['Rating']
byDate = data.groupby('Review Date')[['Company Location', 'Rating']]
byCocoa = data.groupby('Cocoa Percent')['Rating']

first()
second()
