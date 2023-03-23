import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import font_manager
 
#中文字体
my_font = font_manager.FontProperties(family='SimHei')
#显示完整的列
pd.set_option('display.max_columns', None)
 
df = pd.read_csv('IMDB-Movie-Data.csv')

runtime_data = df['Runtime (Minutes)'].values
max_runtime = runtime_data.max()
min_runtime = runtime_data.min()
 
#计算组距
num_bin = (max_runtime-min_runtime)//5
 
#设置图行大小
plt.figure(figsize=(13,6),dpi=80)
#画直方图
plt.hist(runtime_data,num_bin)
 
plt.xticks(range(min_runtime,max_runtime+5,5))
 
#显示
plt.savefig("Time.png")
plt.show()

# rating,runtime分布情况
# 选择图形：直方图
# 准备数据
# runtime_data = df['Runtime (Minutes)'].values
rate_data = df['Rating'].values
max_rate = rate_data.max()
min_rate = rate_data.min()
 
#设置不等宽组距，hist方法中取到的会是一个左闭右开的区间[1,9,3.5)
num_bin_list = [1.9,3.5]
i = 3.5
while i<=max_rate:
    i += 0.5
    num_bin_list.append(i)
print(num_bin_list)
 
#设置图形大小
plt.figure(figsize=(13,6),dpi=80)
#画直方图
plt.hist(rate_data,num_bin_list)
 
#xticks让之前的组距能够对上
plt.xticks(num_bin_list)
 
#显示
plt.savefig("Rating.png")
plt.show()

print(df.info())
print(df.describe())
#获取评分的均分
rate_mean = df.Rating.mean()
print(rate_mean)
#获取导演的人数
print(df.Director.value_counts().count())
print(len(set(df.Director.tolist())))
print(len(df.Director.unique()))
#获取演员的人数
temp_actors_list = df.Actors.str.split(',').tolist()
actors_list = [i for j in temp_actors_list for i in j]
# numpy.array(temp_actors_list).flatten()
actors_num = len(set(actors_list))
print(actors_num)

#统计分类列表
temp_list = df.Genre.str.split(',').tolist()
genre_list = list(set([i for j in temp_list for i in j]))
 
#构造全为0的数组
zero_df = pd.DataFrame(np.zeros((df.shape[0],len(genre_list))),columns=genre_list)
# print(zero_df)
#给每个电影出现分类的位置赋值1
for i in range(df.shape[0]):
    zero_df.loc[i,temp_list[i]] = 1
 
# print(zero_df.head(1))
genre_count = zero_df.sum(axis=0)
print(genre_count)
 
#排序
genre_count = genre_count.sort_values()
_x = genre_count.index
_y = genre_count.values
#画图
plt.figure(figsize=(15,6),dpi=80)
plt.bar(range(len(_x)),_y,width=0.4,color="orange")
plt.xticks(range(len(_x)),_x)
plt.title('电影分类统计图',fontproperties=my_font)
plt.savefig("Classes.png")
plt.show()