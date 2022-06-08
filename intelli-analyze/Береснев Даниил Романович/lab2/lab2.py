import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('./flavors_of_cacao.csv', header=0)

all_rating = data['Rating'].dropna()
all_origin = data['Broad Bean Origin'].dropna()
all_percent = data['Cocoa Percent'].dropna()
all_loc = data['Company Location'].dropna()
all_date = data['Review Date']

convert_percent = []
north_countr = ["Amsterdam", "Austria", "Belgium", "Canada", "Colombia", "Costa Rica", "Czech Republic", "Denmark", "Domincan Republic", "Finland", "France", "Germany", "Ghana", "Grenada", "Guatemala", "Honduras", "Hungary", "Iceland", "India", "Ireland", "Israel", "Italy", "Japan", "Lithuania",
                "Martinique", "Mexico", "Netherlands", "Niacragua", "Nicaragua", "Philippines", "Poland", "Portugal", "Puerto Rico", "Russia", "Sao Tome", "Scotland", "Singapore", "South Korea", "Spain", "St. Lucia", "Suriname", "Sweden", "Switzerland", "U.K.", "U.S.A.", "Venezuela", "Vietnam", "Wales"]

for i in all_percent:
    convert_percent.append(float(i.rstrip('%')))

convert_percent_df = pd.DataFrame(convert_percent, columns=["Cocoa Percent"])

df_bayes = pd.concat([all_loc, all_rating, convert_percent_df], axis=1)

# 2.1
a_bayes = df_bayes.where(df_bayes['Rating'] > 3.1).groupby('Company Location').size().div(
    df_bayes.groupby('Company Location').size())
print("Априорная вероятность выше 3.1")
print(a_bayes)
print("\n")

# 2.2
b_bayes = df_bayes.where(df_bayes['Cocoa Percent'] > 73).groupby('Company Location').size().div(
    df_bayes.groupby('Company Location').size())

ab_bayes = df_bayes.where((df_bayes['Rating'] > 3.1) & (df_bayes['Cocoa Percent'] > 73)).groupby('Company Location').size().div(
    df_bayes.groupby('Company Location').size())

print("Вероятность рейтинга выше 3.1 с содержанием какао 73%\nсреди стран северного полушария")
print((ab_bayes * a_bayes / b_bayes).loc[north_countr])
print("\n")

# 2.3
df_bayes_dates = pd.concat([all_date, all_rating], axis=1)

median_rating = df_bayes_dates.where(df_bayes_dates['Review Date'] > 2010)[
    'Rating'].median()

a_dates = df_bayes_dates.where(df_bayes_dates['Rating'] > median_rating).count().div(df_bayes_dates['Rating'].count())

b_dates = df_bayes_dates.where(df_bayes_dates['Review Date'] > 2014).count().div(df_bayes_dates['Review Date'].count())

ab_dates = df_bayes_dates.where((df_bayes_dates['Review Date'] > 2014) & (
    df_bayes_dates['Rating'] > median_rating)).count().div(df_bayes_dates['Review Date'].count())

print("Вероятность рейтинга после 2014 выше медианного после 2010")
print((a_dates * ab_dates / b_dates)[0])
print("\n")
