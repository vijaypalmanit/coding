import pandas as pd
import numpy as np

# normal datafrmae having date filed which needs to be labeled with corresponding business month
df=pd.DataFrame({'id':[23,45,65,76,21,54],'day':['2019-04-30','2019-05-31','2019-06-29','2019-07-15','2019-10-12','2019-11-22']})

df['day'] = pd.to_datetime(df['day'],format='%Y-%m-%d')

# this is dataframe consist of month ending for each business month eg. Business month May last from 2019-04-29 --- 2019-05-25 and so on....
df2=pd.DataFrame({'month_ending':['2019-04-28','2019-05-25','2019-06-29','2019-07-27','2019-08-24','2019-09-28','2019-10-26','2019-11-23','2019-12-28','2020-01-25','2020-02-22','2020-03-28','2020-05-02']})
df2['month_ending']=pd.to_datetime(df2['month_ending'])

bned_months=['May','June','July','Aug','Sep','Oct','Nov','Dec','Jan','Feb','Mar','Apr']

df['month'] = pd.cut(df.day.astype(np.int64)//10**9,
                   bins=df2.month_ending.astype(np.int64)//10**9,
                   labels=bned_months)

print(df)