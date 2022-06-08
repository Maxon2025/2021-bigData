import pandas as pd

df = pd.read_csv('../flavors_of_cacao.csv')
south_countries = ['Australia', 'Argentina', 'Bolivia', 'Peru', 'Brazil', 'Chile', 'Colombia','Ecuador', 'Madagascar', 'New Zealand', 'Sao Tome', 'Fiji']
#-----------------------------------------------1 пункт----------------------------------------------------------
df1 = df.groupby(by=['Company Location'])['Company Location'].unique()
s = 0
var = 0
pa = pd.DataFrame(columns=['Country', 'Probability'])
for i in df1.index:
    for n in df['Company Location'].index:
        if df.at[n, 'Company Location'] == df1.at[i]:
            s += 1
            if df.at[n, 'Rating'] > 3.1:
                var += 1
    new_row = {'Country': df1.at[i], 'Probability': var/s}
    pa = pa.append(new_row, ignore_index=True)
    s = 0
    var = 0

print('Общая вероятность по всем странам, что рейтинг > 3,1')
print(pa)
print()
#-----------------------------------------------2 пункт----------------------------------------------------------
a=df[(df['Company Location'].isin(south_countries)) & (df['Rating'] > 3.1)& (df['Cocoa Percent'].replace('%', '', regex=True).astype('float32') > 73)].count()['Rating']
b=df[(df['Company Location'].isin(south_countries)) & (df['Cocoa Percent'].replace('%', '', regex=True).astype('float32') > 73)].count()['Rating']
P=a/b
print("Вероятность того, что новый сорт какао с содержанием выше 73% (Cocoa Percent) будет имет оценку выше 3.1 для стран южного полушария: "+P.astype('str'))
print()
#-------------------------------------------------3 пункт---------------------------------------------------------
mediana=df[df['Review Date']>2010]['Rating'].median()

all_znach=df[(df['Review Date']>2014)].count()['Rating']
med_znach=df[(df['Review Date']>2014) & (df['Rating'] > mediana)].count()['Rating']
print("Вероятность того, что обзоры какао после 2014 года будут иметь оценку выше медианной по всему периоду после 2010 года: "+ (med_znach/all_znach).astype('str'))



