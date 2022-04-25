import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def generateDataTable(rawData):
    noneGroup = pd.concat([rawData[rawData['attacker_1'].isnull()==True], rawData[rawData['attacker_2'].isnull()==False]], axis=0)

    rawData = rawData[rawData['attacker_1'].isnull()==False][data['attacker_2'].isnull()==True]

    groupedBattles = rawData.groupby('attacker_1',as_index=False)['name'].count()

    dataTable = {'House':np.append(groupedBattles['attacker_1'], 'None'),'Number of battles':np.append(groupedBattles['name'], noneGroup['attacker_1'].count())}
    
    return dataTable

def showDiagram(dataTable):
    fig, ax = plt.subplots()

    ax.pie(dataTable['Number of battles'], labels=dataTable['House'], wedgeprops=dict(width=0.5), shadow=True)
    plt.show()

def showDataTable(dataTable):
    fig, ax = plt.subplots()
    fig.tight_layout()
    fig.patch.set_visible(False)
    ax.axis('off')
    ax.axis('tight')

    dataFrame = pd.DataFrame(dataTable, columns=("House","Number of battles"))

    ax.table(cellText=dataFrame.values, colLabels=dataFrame.columns, loc='center', cellLoc="left")
    plt.show()

data = pd.read_csv('../_lab-2/GoT/battles.csv', header=0)

table = generateDataTable(data)

showDiagram(table)

showDataTable(table)
