#%% [markdown]
# #pandas入门

#%%
import pandas as pd
from pandas import Series,DataFrame

#%% [markdown]
# #1. pandas的数据结构介绍
#%%
# 要使用pandas，需要熟悉两个主要数据结构：Series和DataFrame
obj=pd.Series([4,7,-5,3])
print(obj)
print(obj.values)
print(obj.index)

obj2=pd.Series([4,7,-5,3],index=['d','b','a','c'])
print(obj2)
print(obj2.index)
print(obj2['a'])

obj2['d']=6
print(obj2[['c','a','d']])

# 使用Numpy函数或类似Numpy的运算都会保留索引值的链接
print(obj2[obj2>0])
# print(obj2*2)

import numpy as np

print(np.exp(obj2))
print('b' in obj2)
print('e' in obj2)

#%%
# 如果数据被存放在一个python字典中，可以直接通过这个字典来创建Series
sdata={'Ohio':35000,'Texas':71000,'Oregon':16000,'Utah':5000}
obj3=pd.Series(sdata)
obj3

#%%
# 可以通过传入排好序的字典的键来改变顺序
states=['California','Ohio','Oregon','Texas']
obj4=pd.Series(sdata,index=states)
obj4

#%%
# pandas的isnull和notnull函数可用于检测缺失数据
print(pd.isnull(obj4))
print(pd.notnull(obj4))
print(obj4.isnull())

#%% 
# Series最重要的一个功能，根据运算的索引标签来自动对齐数据
print(obj3)
print(obj4)
print(obj3+obj4)

#%%
# Series对象本身及其索引都有一个name属性
obj4.name='population'
obj4.index.name='state'
print(obj4)

#%%
obj.index=['Bob','Steve','Jeff','Ryan']
print(obj)

#%% [markdown]
# ## DataFrame
data={'state':['Ohio','Ohio','Ohio','Nevada','Nevada','Nevada'],'year':[2000,2001,2002,2001,2002,2003],'pop':[1.5,1.7,3.6,2.4,2.9,3.2]}
frame=pd.DataFrame(data)
frame
#%%
# 对于特别大的DataFrame,head方法会选取前五行
frame.head()

#%%
# 如果制定了列序列，则DataFrame的列就会按照指定顺序进行排列
pd.DataFrame(data,columns=['year','state','pop'])

#%%
frame2=pd.DataFrame(data,columns=['year','state','pop','debt'])
frame2
#%%
frame2.columns

#%%
frame2['state']

#%%
frame2.year

#%%
# 行也可以通过为止或者名称的方式进行获取，比如loc属性
frame2.loc[2]

#%%
frame2['debt']=16.5
frame2

#%%
frame2['debt']=np.arange(6.)
frame2
#%%
val=pd.Series([-1.2,-1.5,-1.7],index=['two','four','five'])
frame2['debt']=val
frame2

#%%
frame2['eastern']=frame2.state=='Ohio'
frame2
# 不能用frame2.eastern创建新的列
#%%
del frame2['eastern']
frame2.columns

#%%
pop={'Nevada':{2001:2.4,2002:2.9},'Ohio':{2000:1.5,2001:1.7,2002:3.6}}
frame3=pd.DataFrame(pop)
frame3
#%%
frame3.T

#%%
pd.DataFrame(pop,index=[2001,2002,2003])
pdata={'Ohio':frame3['Ohio'][:-1],'Nevada':frame3['Nevada'][:2]}
pd.DataFrame(pdata)

#%%
# ## 索引对象
obj=pd.Series(range(3),index=['a','b','c'])
index=obj.index
index

#%%
# index对象是不可变的，因此用户不能对其进行修改
index[1:]

#%%
labels=pd.Index(np.arange(3))
labels

#%%
obj2=pd.Series([1.5,-2.5,0],index=labels)
obj2

#%%
obj2.index is labels

#%%
frame3

#%%
frame3.columns

#%%
'Ohio' in frame3.columns

#%%
2003 in frame3.index

#%%
dup_labels=pd.Index(['foo','foo','bar','bar'])
dup_labels

#%% [markdown]
# # 2.基本功能
# ## 重新索引
