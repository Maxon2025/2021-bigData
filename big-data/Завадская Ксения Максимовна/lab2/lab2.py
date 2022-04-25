import pandas
import matplotlib.pyplot as plt
import numpy

data = pandas.read_csv('../_lab-2/GoT/battles.csv', header=0)

data['attacker_2'] = data['attacker_2'].str.len()
noneValue = data[data['attacker_2'].isnull() == False]['attacker_2'].count()
data = data.loc[data['attacker_2'].isnull()]
values = data.groupby('attacker_1', as_index=False)['name'].count()

labels = numpy.append(values['attacker_1'], 'None')
values = numpy.append(values['name'], noneValue)

fig, ax = plt.subplots()
s1 = pandas.Series(labels, name='Houses')
s2 = pandas.Series(values, name='Battles_Absolute')
s3 = pandas.Series(values * 100 / values.sum(), name='Battles_Normal')

print(pandas.concat([s1, s2, s3], axis=1))
ax.pie(values, labels=labels)
plt.show()