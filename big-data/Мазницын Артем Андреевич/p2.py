import pandas as pd
import matplotlib.pyplot as plt
import numpy

data = pd.read_csv('../_lab-2/GoT/battles.csv', header=0)
data = data[['year', 'attacker_king']]
data['attacker_king'] = data['attacker_king'].str.len()
x = data['year'].unique()

Len = data.groupby('year', as_index=False)['attacker_king'].sum()
y1 = data.groupby('year')['attacker_king'].sum()
fullCount = data['attacker_king'].sum()
y2 = data.groupby('year')['attacker_king'].sum() * 100 / fullCount

print('Введите abs для отображения таблицы в абсолютных значениях, для таблицы в нормированных введите что-нибудь другое.')
if input() == 'abs':
    plt.bar(x, y1)
else:
    plt.bar(x, y2)
    plt.ylim([0, 100])

namesLength = pd.merge(y2, Len[["year", "attacker_king"]], on="year", how="left")
print(namesLength)
plt.xlabel('Years')
plt.ylabel('Names length')
plt.grid()
plt.show()