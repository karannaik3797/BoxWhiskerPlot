import csv
import pandas as pd

data = pd.read_csv('data/mc1-reports-data.csv',parse_dates=['time'])
data['mean'] = data.iloc[:,[1,2,3,4,5]].mean(axis=1)
data = data.sort_values('time')
data = data.drop(['sewer_and_water','power','roads_and_bridges','medical','buildings','shake_intensity'],axis=1)
data.count()
data.to_csv('data/mean.csv',index=False)