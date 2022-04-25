import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def func1(data):
    attacker = data.groupby(['attacker_king', 'year'], dropna=True)[['year']]
    attacker.agg('count').to_csv('l2', sep=',')
    print(attacker.agg('count'))
    print(" ")
    defender = data.groupby(['defender_king', 'year'], dropna=True)[['year']]
    defender.agg('count').to_csv('l22', sep=',')
    print(defender.agg('count'))
    print(" ")

    df1 = pd.read_csv('l2', header=0, sep=',', na_filter=True, names=['king', 'year', 'count'])
    df2 = pd.read_csv('l22', header=0, sep=',', na_filter=True, names=['king', 'year', 'count'])
    df3 = pd.concat([df1, df2], axis=0, ignore_index=True)
    df3.to_csv('222', sep=',')
    print(df3)
    print(" ")
    df4 = df3.groupby(['king', 'year'], dropna=True)[['count']]
    df4.agg('sum').to_csv('exit', sep='\t')
    df4 = pd.read_csv('exit', header=0, sep='\t', na_filter=True, names=['king', 'year', 'count'])
    print(df4)
    return df4

def graf1(df):
    # make the data
    np.random.seed(3)
    x = df['year']
    y = df['king']
    # size and color:
    sizes = df['count'] * 8
    colors = np.random.uniform(15, 80, len(x))
    # plot
    fig, ax = plt.subplots()
    ax.scatter(x, y, s=sizes, c=colors, vmin=0, vmax=200)
    # zip joins x and y coordinates in pairs
    for x1, y1, s1 in zip(x, y, sizes):
        label = round((s1 / 8) / df['count'].agg('sum'), 3)
        plt.annotate(label,  # this is the text
                     (x1, y1),  # these are the coordinates to position the label
                     textcoords="offset points",  # how to position the text
                     xytext=(0, 5),  # distance from text to points (x,y)
                     ha='center')  # horizontal alignment can be left, right or center

    ax.set(xlim=(297, 301), xticks=np.arange(298, 301))
    plt.show()

def graf2(df):
    # make the data
    np.random.seed(3)
    x = df['year']
    y = df['king']
    # size and color:
    sizes = df['count'] * 8
    colors = np.random.uniform(15, 80, len(x))
    # plot
    fig, ax = plt.subplots()
    ax.scatter(x, y, s=sizes, c=colors, vmin=0, vmax=200)
    # zip joins x and y coordinates in pairs
    for x1, y1, s1 in zip(x, y, sizes):
        label = int(s1/8)
        plt.annotate(label,  # this is the text
                     (x1, y1),  # these are the coordinates to position the label
                     textcoords="offset points",  # how to position the text
                     xytext=(0, 7),  # distance from text to points (x,y)
                     ha='center')  # horizontal alignment can be left, right or center

    ax.set(xlim=(297, 301), xticks=np.arange(298, 301))
    plt.show()

data = pd.read_csv('../_lab-2/GoT/battles.csv', header=0)
print(data.head())
k = '0'
while k != 3:
    k = input("Введите 1 для получения графика со значениями; 2 для графика с процентами; 3 для выхода.", )
    if k == '1':
        graf1(func1(data))
    if k == '2':
        graf2(func1(data))
    if k == '3':
        break
    else:
        print("Значение неверное. Попробуйте снова.")