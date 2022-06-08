import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("flavors_of_cacao.csv")
df = df.dropna()
df['Cocoa Percent'] = df['Cocoa Percent'].dropna().str.strip('%').astype(float) / 100
print(df)
print(df.info())


byData = df.sort_values(["Review Date"]).groupby(["Review Date"])["Rating"]
fig, axs = plt.subplots(2)

axs[0].plot(byData.mean(), color='r', label='Среднее(груп)')
axs[0].axhline(df['Rating'].mean(), color='r', linestyle='--', label='Среднее(общ)')
axs[0].plot(byData.median(), color='c', label='Медианное(груп)')
axs[0].axhline(df['Rating'].median(), color='c', linestyle='--', label='Медианное(общ)')
axs[0].legend()

axs[1].plot(byData.var(), color='g', label='Дисперсия(груп)')
axs[1].axhline(df['Rating'].var(), color='g', linestyle='--', label='Дисперсия(общ)')
axs[1].plot(byData.std(), color='orchid', label='СКО(груп)')
axs[1].axhline(df['Rating'].std(), color='orchid', linestyle='--', label='СКО(общ)')
axs[1].legend()

plt.show()

byCp = df.sort_values(['Cocoa Percent']).groupby('Cocoa Percent')['Rating']
plt.plot(byCp.mean(), color='b', label='Рейтинг')
plt.plot(byCp.min(), color='g', label='Мин')
plt.plot(byCp.max(), color='r', label='Макс')
plt.plot(byCp.var(), color='k', label='Дисперсия')
plt.xlabel('Содержание какао (%)')
plt.ylabel('Рейтинг')
plt.legend()
plt.show()
