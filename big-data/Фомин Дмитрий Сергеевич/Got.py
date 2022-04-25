import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import numpy as np

data = pd.read_csv('../_lab-2/GoT/battles.csv',header=0)

def lab2(data,norm):
    defenders = data['defender_1'].dropna().unique()    
    
    dataCollector=pd.DataFrame(data=None)

    for i in defenders:
        y=data.loc[data['defender_1'] == i].groupby('year')['battle_number'].nunique(dropna=True)
        dataCollector=pd.concat([dataCollector,y],axis=1)
    
    dataCollector.columns = defenders   
    
    if(norm):
        summ = 1
        for i in range(dataCollector.shape[0]):
            for j in range(dataCollector.shape[1]):
                if (not np.isnan(dataCollector.iloc[i,j])):
                    summ+=dataCollector.iloc[i,j]
        
        pd.options.display.max_columns=20
        print(dataCollector)

        for i in range(dataCollector.shape[0]):
            for j in range(dataCollector.shape[1]):
                if (not np.isnan(dataCollector.iloc[i,j])):
                    dataCollector.iloc[i,j]=round(dataCollector.iloc[i,j]/(summ/100),1)



    graph = dataCollector.plot(kind = 'bar', stacked=True, colormap='Paired')
    
    graph.set_xlabel("Год")
    if (norm):
        graph.set_ylabel("Процент битв")
    else:
         graph.set_ylabel("Количество битв")   
    
    
    for i in range(data['defender_1'].dropna().nunique()):           
        graph.bar_label(graph.containers[i],label_type='center')

    plt.show()
    return None

lab2(data,False)
lab2(data,True)



