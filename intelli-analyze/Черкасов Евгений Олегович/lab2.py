import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()


def p(data, cond, selecter='Rating', group='Company Location'):
    df = data.query(cond)
    if group is not None:
        data = data.groupby(group)
        df = df.groupby(group)
    return df[selecter].count() / data[selecter].count()


def plot(data, name):
    plt.subplots(figsize=(12, 7))
    ax = sns.barplot(x=data.index, y=data.array, palette='deep')

    ax.set_title(name)
    ax.set_xticklabels(labels=data.index, rotation=90)

    plt.show()


def first(data):
    p_ = p(data, 'Rating > 3.1').dropna()
    plot(p_, 'Вероятность получения оценки выше 3.1')


def second(data):
    america = ['Argentina', 'Bolivia', 'Brazil', 'Canada', 'Chile',
               'Colombia', 'Ecuador', 'Guatemala', 'U.S.A.', 'Venezuela']
    p_ = p(data, 'Rating > 3.7 and `Cocoa Percent` > 73') / p(data, '`Cocoa Percent` > 73')
    p_ = p_[america]

    plot(p_, 'Условная вероятность получения оценки выше 3.1 при содержании какао выше 73%')


def third(data):
    df = data.query('`Review Date` > 2014')
    median = data.query('`Review Date` > 2010')['Rating'].median()
    p_ = p(df, f'Rating > {median}', group=None)

    print('Вероятность того, что все обзоры какао после 2014 года будут '
      'иметь оценку выше медианной по всему периоду после 2010: ', p_)


def main():
    data = pd.read_csv('flavors_of_cacao.csv')
    data['Cocoa Percent'] = data['Cocoa Percent'].replace('%', '', regex=True).astype('float32')

    first(data)
    second(data)
    third(data)


if __name__ == '__main__':
    main()
