
from pandas import read_csv
import numpy as np
import pandas
ds = read_csv('E:\AIProject\day7\salariesNoisy.csv')
ds = pandas.DataFrame(ds,columns=[0,1,2,3,4,5,6])
print(ds.isnull().any())
print(ds.isnull().sum())
print(ds.isnull().sum().sum())
print( ds[6] .isnull() .sum())
ds[6] = ds[6].fillna('no view')
print(ds[6].isnull().sum())
ds.to_csv('fille1.csv')
print(ds[ds[3]<=0])
print(ds[ds[3]<=0][3].count())
df=pandas.DataFrame(
    [[np.nan,72,67],
     [23,np.nan,62],
     [37,74,np.nan]],
    columns=['a','b','c']
)
df_res=df.fillna(value={'a':0,'b':1,'c':2})
print('orignal Data \n',df)
print('\nresulte data \n',df_res)

pandas.DataFrame()
