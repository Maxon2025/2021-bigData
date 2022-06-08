import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns;

sns.set()


def priority(df, predicate, group=None):
    filtered = df[predicate(df)]
    if group is not None:
        filtered = filtered.groupby(group)
        df = df.groupby(group)
    return filtered.count() / df.count()


def conditional_priority(df, predicate_ab, predicate_b, group=None):
    return priority(df, predicate_ab, group) / priority(df, predicate_b, group)


def plot(data, name):
    plt.subplots(figsize=(12, 7))
    ax = sns.barplot(x=data.index, y=data.array, palette='deep')

    ax.set_title(name)
    ax.set_xticklabels(labels=data.index, rotation=90)

    plt.show()


def pl(data):
    fig, ax = plt.subplots(2, 2, figsize=(12, 10))

    for ax_, data_ in zip(np.concatenate(ax), np.split(data, 4)):
        sns.barplot(x=data_.index, y=data_.array, ax=ax_)
        ax_.set_xticklabels(labels=data_.index, rotation=-15)
        ax_.set_xlabel('')

    plt.show()


data = pd.read_csv('flavors_of_cacao.csv')
data['Cocoa Percent'] = data['Cocoa Percent'].replace('%', '', regex=True).astype('float32')

p_1 = priority(data, lambda x: x['Rating'] > 3.7, 'Company Location')['Rating'].dropna()
pl(p_1)


p_2 = conditional_priority(data,
                           lambda x: (x['Rating'] > 3.7) & (x['Cocoa Percent'] > 73),
                           lambda x: x['Cocoa Percent'] > 73,
                           'Company Location')['Rating']

countries = ['Amsterdam', 'Austria', 'Belgium', 'Denmark', 'France', 'Germany', 'Hungary', 'Iceland', 'Italy', 'Lithuania', 'Madagascar', 'Poland', 'Sao Tome', 'Scotland', 'Spain', 'Switzerland', 'U.K.']
p_2 = p_2[countries].fillna(0)
plot(p_2, 'Rating >3.1 | Cocoa Percent >73')


median = data[data['Review Date'] > 2010]['Rating'].median()
p_3 = conditional_priority(data,
                           lambda x: (data['Rating'] > median) & (data['Review Date'] > 2014),
                           lambda x: data['Review Date'] > 2014)['Rating']

print('Rating > median | Review Date > 2014: ', p_3)
