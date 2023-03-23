"""
绘制北京PM2.5随时间的变化情况（中美报告）
"""
import pandas as pd
from matplotlib import pyplot as plt
 
pd.set_option('display.max_columns',None)
 
df = pd.read_csv('BeijingPM20100101_20151231.csv')
# print(df.head())
 
#把分开的时间字符串通过periodIndex的方法转化为pandas的时间类型
period = pd.PeriodIndex(year=df.year,month=df.month,day=df.day,hour=df.hour,freq='H')
df['datetime'] = period
print(df.head(10))
 
#把datetime设置为索引
df.set_index('datetime',inplace=True)
 
#进行降采样
df = df.resample('7D').mean()
 
#处理缺失值，删除缺失数据
# data = df['PM_US Post'].dropna()
# china_data = df['PM_Nongzhanguan'].dropna()
data = df['PM_US Post']
china_data = df['PM_Nongzhanguan']
 
#画图
_x = data.index
_y = data.values
 
_x_china = china_data.index
_y_china = china_data.values
 
plt.figure(figsize=(13,8),dpi=80)
 
plt.plot(range(len(_x)),_y,label='US_POST',alpha=0.7)
plt.plot(range(len(_x_china)),_y_china,label='CN_POST',alpha=0.7)
 
plt.xticks(range(0,len(_x_china),10),list(_x_china.strftime('%Y%m%d'))[::10],rotation=45)
plt.savefig("beijing.png")
plt.show()