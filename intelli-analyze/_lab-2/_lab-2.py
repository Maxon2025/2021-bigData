import pandas as pd

df = pd.read_csv('../_lab-1/flavors_of_cacao.csv')

def bayes(pA, pB, pBA):
    return pBA*pA/pB

a = .31 #вероятность, что событие А вообще происходит
ba = .8 # вероятность, что событие В происходит при подтверждении события А
bna = .15 # событие В происходит, когда точно не происходит событие А
b = ba*a + bna*(1-a) # общая вероятность события В

print(bayes(a, b, ba))

# пара примеров как получать статистические данные
dt = df.groupby("Review Date")["Rating"].mean()
# по году оценки раньше 2014
a = dt.apply(lambda x: True if x>3.2 else False)
pa = len(a[a==True].index)/len(a.index)
b = dt[dt.index<2014].apply(lambda x: True if x>3.2 else False)
pb = len(b[b==True].index)/len(b.index)

# по принадлежности стран к списку
foo_true = lambda x: True if x>3.2 else False
south_countries = ['Australia', 'Puerto Rico', 'Venezuela', 'Colombia'] # неполный список

dt2 = df.groupby('Company Location')['Rating'].mean()
A = dt2.apply(foo_true)
pA = len(A[A==True].index)/len(A.index)
print(f'All rating above 3.2: {pA}')
B = dt2.loc[south_countries].apply(foo_true)
pB = len(B[B==True].index)/len(B.index)
print(f'Only south rating above 3.2: {pB}')

print('Number of countries in south where rating is above 3.3')
print(df[(df['Company Location'].isin(south_countries)) & (df['Rating'] > 3.3)].count()['Rating'])
