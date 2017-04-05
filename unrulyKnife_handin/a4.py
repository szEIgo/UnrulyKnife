import numpy as np
from operator import itemgetter
import matplotlib.pyplot as plt
import pandas as pd
import urllib.request
import operator
from bokeh.charts import Donut, show

df = pd.read_csv('http://data.kk.dk/dataset/9070067f-ab57-41cd-913e-bc37bfaf9acd/resource/9fbab4aa-1ee0-4d25-b2b4-b7b63537d2ec/download/befkbhalderkoencivst.csv', encoding='latin1').fillna(0)

#Create two piecharts, showing the distribution of marital status' in bydel 1, 2 and 3 in year 2000 and 2015

df_2000 = df[(df['AAR'] == 2000) & (df['BYDEL'] < 4)]
df_2000.groupby(['CIVST', 'BYDEL', 'AAR'])['PERSONER'].sum()
data_2000 = df_2000['CIVST'].value_counts()
print(data_2000)

x,y = zip(*sorted(data_2000.items(),key=operator.itemgetter(1)))
pie1_data = pd.Series(y,x)

pie1_chart = Donut(pie1_data)
show(pie1_chart)



df_2015 = df[(df['AAR'] == 2015) & (df['BYDEL'] < 4)]
df_2015.groupby(['CIVST', 'BYDEL', 'AAR'])['PERSONER'].sum()
data_2015 = df_2015['CIVST'].value_counts()
print(data_2015)

x2,y2 = zip(*sorted(data_2015.items(),key=operator.itemgetter(1)))
pie2_data = pd.Series(y2,x2)

pie2_chart = Donut(pie2_data)
show(pie2_chart)





#df4 = df.groupby(["AAR", "BYDEL", "CIVST"], as_index=False)["PERSONER"].sum()
#print(df4[:5])
#df4 = df4[(df4.BYDEL < 4)& (df4.AAR == 2000)]
#print(df4[:5])
#Deleting columns. Pass the axis=1 option for it to work on columns and not rows.
#df4 = df4.drop(['BYDEL','AAR'], axis=1)
#print(df4[:5])
#df4 = df4.groupby('CIVST').sum()
#print(df4[:5])
#Removing the 3 minor values that contains around 1k value total (less than 1%)
#df4 = df4.nlargest(4, 'PERSONER')
#print(df4[:5]
