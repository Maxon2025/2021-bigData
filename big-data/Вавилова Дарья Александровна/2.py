import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def Map():
    at_k = data['attacker_king'].dropna()
    def_k = data['defender_king'].dropna()
    all_k = pd.concat([at_k, def_k])
    all_k = all_k.unique()

    df = pd.DataFrame(data=None)

    for i in all_k:
        df_ch = data.loc[(data['attacker_king'] == i) | (data['defender_king'] == i)].groupby('year')[
            'battle_number'].nunique(dropna=True)
        df = pd.concat([df, df_ch], axis=1)

    df.columns = all_k
    df = df.fillna(0)
    return df, all_k


def Graph(df,st):
    year = df.index.array
    fig, ax = plt.subplots()
    im = ax.imshow(df)

    ax.set_xticks(np.arange(len(all_k)))
    ax.set_yticks(np.arange(len(year)))

    ax.set_yticklabels(year)
    ax.set_xticklabels(all_k)

    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")

    plt.ylabel('Год', loc='top', rotation=0)

    for i in range(len(year)):
        for j in range(len(all_k)):
            text = ax.text(j, i, str(df.iloc[i][j])+ st,
                           ha="center", va="center", color="black")

    ax.set_title("Количество битв")
    fig.tight_layout()

    return None

data = pd.read_csv('C:/Users/ACER/OneDrive/Документы/GitHub/2021-bigData/_lab-2/GoT/battles.csv', header=0)

df, all_k = Map()
df_per = (df / df.sum().sum() * 100).round(2)
pd.options.display.max_columns = 20
print(pd.concat([df, df_per], axis=1))

Graph(df,'')
Graph(df_per,'%')
plt.show()
