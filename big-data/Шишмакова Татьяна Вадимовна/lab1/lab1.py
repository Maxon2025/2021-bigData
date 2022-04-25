import numpy as np
import pandas as pd
from math  import factorial

rng = np.random.default_rng()
df1 = pd.DataFrame(rng.integers(-1000,5000,size = (9000,4)))
df2 = pd.DataFrame(rng.random((9000,3)))
df = pd.concat([df1,df2],axis = 1)
df.columns = [x for x in range(0,7)]
df.to_csv('shishmakova_1', sep='\t',index=False)
print(df.head(10))

def fact(x):
    if x<2:
        return 1
    else:
        return x*fact(x-1)

def process_data(df):
    medium_value= sum(df[4] + df[5] + df[6])/(len(df[4]) + len(df[5]) + len(df[6]))
    print('Medium 4:6: ', medium_value)
    min_int_value = (sum(df[0]) + sum(df[1]) + sum(df[2]) + sum(df[3])) % 100
    print(min_int_value)
    print('Factorial of min % 100 of 0:4: ', factorial(min_int_value))

process_data(df)

for i in range(100):
    df.at[np.random.randint(0,9000),0] = -2000
    df.at[np.random.randint(0,9000),3] = None
    df.at[np.random.randint(0,9000),1] = 1

df.to_csv('shishmakova_2', sep='\t',index=False)
print(df.head(10))

def map_data(df):
    #df.isnull
    #df.ge
    #df.dtypes
    #df.empty

    df_int = df[df.isin(range(-1000, 5000))]      #isin()Метод Pandas используется для фильтрации данных/проверяет, содержится ли каждый элемент в указанных значениях/Если элемент присутствует - True, иначе False
    df_int.fillna(value=0, inplace=True)          #Функция fillna() автоматически найдет и заменит все значения NaN в DataFrame
    #удаляем int значения в 4-7 столбцах
    df_int.drop(df_int.iloc[:, 4:7], axis=1, inplace=True)  #Drop () удаляет указанные метки из строк или столбцов/iloc() получаем конкретное значение, принадлежащее строке и столбцу(все строки с 4,5,6 столбцов)/axic=1 выполняется по горизонтали
    df_int = df_int.convert_dtypes()

    df_float = df[(df<1.)&(df>-1.)]
    df_float.fillna(value=0, inplace=True)
    #удаляем float значения в 1-3 столбцах
    df_float.drop(df_float.iloc[:, :4], axis=1, inplace=True)

    df_filtered = pd.concat([df_int, df_float], axis=1)
    df_filtered.to_csv('shishmakova_3', sep='\t',index=False)
    print('filtered /----------------/')
    print(df_filtered)
    #return df_filtered   #возвращение в виде таблицы

map_data(df)
