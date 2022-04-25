import pandas
import matplotlib.pyplot as plt
import numpy

data = pandas.read_csv('../_lab-2/GoT/battles.csv', header=0)
data = data[['year', 'attacker_king']]
data['attacker_king'] = data['attacker_king'].str.len()
years = data['year'].unique()

namesLength11 = data.groupby('year', as_index=False)['attacker_king'].sum()
namesLength12 = data.groupby('year')['attacker_king'].sum()
totalNum = data['attacker_king'].sum()
namesLength2 = data.groupby('year')['attacker_king'].sum() * 100 / totalNum

print('Какой график вы хотите увидеть? В абсолютных значениях - введите 1, в нормированных - любое другое значение.')
if input() == '1':
    plt.bar(years, namesLength12)
else:
    plt.bar(years, namesLength2)
    plt.ylim([0, 100])

namesLength = pandas.merge(namesLength2, namesLength11[["year", "attacker_king"]], on="year", how="left")
namesLength = namesLength.rename(columns={'attacker_king_x': 'normalized_values', 'attacker_king_y': 'absolute_values'})
print(namesLength)

plt.title('График зависимости')
plt.xlabel('Года')
plt.ylabel('Сумма длины имён')
plt.grid()
plt.show()