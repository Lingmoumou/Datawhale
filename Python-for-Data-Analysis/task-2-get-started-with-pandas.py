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
obj=pd.Series([4.5,7.2,-5.3,3.6],index=['d','b','a','c'])
obj

#%%
obj2=obj.reindex(['a','b','c','d','e'])
obj2

#%%
obj3=pd.Series(['blue','purple','yellow'],index=[0,2,4])
obj3

#%%
obj3.reindex(range(6),method='ffill')

#%%
# reindex可以修改行索引和列
frame=pd.DataFrame(np.arange(9).reshape((3,3)),index=['a','b','c'],columns=['Ohio','Texas','California'])
frame

#%%
frame2=frame.reindex(['a','b','c','d'])
frame2

#%%
states=['Ohio','Texas','California']
frame.reindex(columns=states)

#%%
# ##丢弃指定轴上的项
obj=pd.Series(np.arange(5.),index=['a','b','c','d','e'])
obj

#%%
new_obj=obj.drop('c')
new_obj

#%%
obj.drop(['d','e'])

#%%
data=pd.DataFrame(np.arange(16).reshape((4,4)),index=['Ohio','Colorado','Utah','New York'],columns=['one','two','three','four'])
data

#%%
data.drop('two',axis=1)

#%%
data.drop(['two','four'], axis='columns')

#%%
obj.drop('c',inplace=True)
obj

#%%
# ##索引、选取和过滤
obj=pd.Series(np.arange(4.),index=['a','b','c','d'])
obj

#%%
obj['b']

#%%
obj[1]

#%%
obj[2:4]

#%%
obj[['b','a','d']]

#%%
obj[[1,3]]

#%%
obj[obj<2]

#%%
# 用标签起算与普通的python切片不同，其末端是包含的
obj['b':'c']

#%%
obj['b':'c']=5
obj

#%%
data=pd.DataFrame(np.arange(16).reshape((4,4)),index=['Ohio','Colorado','Utah','New York'],columns=['one','two','three','four'])
data

#%%
data['two']

#%%
data[['three','one']]

#%%
# 索引的几个特殊的情况
# 通过切片或布尔型数组选取数据
data[:2]

#%%
data[data['three']>5]

#%%
# 通过布尔型DataFrame选取数据
data<5

#%%
data[data<5]=0
data

#%%
# ##用loc和iloc进行选取
# loc:轴标签，iloc整数索引
data.loc['Colorado',['two','three']]

#%%
data.iloc[2,[3,0,1]]

#%%
data.iloc[2]

#%%
data.iloc[[1,2],[3,0,1]]

#%%
data.loc[:'Utah','two']

#%%
data.iloc[:,:3][data.three>5]

#%%
# ##整数索引
ser=pd.Series(np.arange(3.))
ser

#%%
ser2=pd.Series(np.arange(3.),index=['a','b','c'])
ser2[-1]

#%%
ser[:1]

#%%
ser.loc[:1]

#%%
ser.iloc[:1]

#%%
# ##算数运算和数据对齐
s1=pd.Series([7.3,-2.5,3.4,1.5],index=['a','c','d','e'])
s2=pd.Series([-2.1,3.6,-1.5,4,3.1],index=['a','c','e','f','g'])
s1

#%%
s2

#%%
s1+s2

#%%
df1=pd.DataFrame(np.arange(9.).reshape((3,3)),columns=list('bcd'),index=['Ohio','Texas','Colorado'])
df2=pd.DataFrame(np.arange(12.).reshape((4,3)),columns=list('bde'),index=['Utah','Ohio','Texas','Oregon'])
df1

#%%
df2

#%%
df1+df2

#%%
df1=pd.DataFrame({'A':[1,2]})
df2=pd.DataFrame({'B':[3,4]})
df1

#%%
df2

#%%
df1-df2

#%%
# ##在算数方法中填充值
df1=pd.DataFrame(np.arange(12.).reshape((3,4)),columns=list('abcd'))
df2=pd.DataFrame(np.arange(20.).reshape((4,5)),columns=list('abcde'))
df2.loc[1,'b']=np.nan
df1

#%%
df2

#%%
df1.add(df2,fill_value=0)

#%%
1/df1

#%%
# 以r开头，他会翻转参数
df1.rdiv(1)

#%%
df1.reindex(columns=df2.columns,fill_value=0)

#%%
# ## DataFrame和Series之间的运算
arr=np.arange(12.).reshape((3,4))
arr

#%%
arr[0]

#%%
arr-arr[0]

#%%
frame=pd.DataFrame(np.arange(12.).reshape((4,3)),columns=list('bde'),index=['Utah','Ohio','Texas','Oregon'])
series=frame.iloc[0]
frame

#%%
series

#%%
frame-series

#%%
series2=pd.Series(range(3),index=['b','e','f'])
frame+series2

#%%
series3=frame['d']
frame

#%%
series3

#%%
frame.sub(series3,axis='index')

#%%
# ##函数应用和映射
frame=pd.DataFrame(np.random.randn(4,3),columns=list('bde'),index=['Utah','Ohio','Texas','Oregon'])
frame

#%%
np.abs(frame)

#%%
# 将函数应用到各行或列所形成的一维数组上，apply方法即可实现此功能
f=lambda x:x.max()-x.min()
frame.apply(f)

#%%
frame.apply(f,axis='columns')

#%%
def f(x):
    return pd.Series([x.min(),x.max()],index=['min','max'])

frame.apply(f)

#%%
format=lambda x:'%.2f' % x
frame.applymap(format)

#%%
frame['e'].map(format)

#%%
# ##排序和排名
obj=pd.Series(range(4),index=['d','a','b','c'])
obj.sort_index()

#%%
frame=pd.DataFrame(np.arange(8).reshape((2,4)),index=['three','one'],columns=['d','a','b','c'])
frame.sort_index()

#%%
frame.sort_index(axis=1)

#%%
frame.sort_index(axis=1,ascending=False)

#%%
obj=pd.Series([4,7,-3,2])
obj.sort_values()

#%%
obj=pd.Series([4,np.nan,7,np.nan,-3,2])
obj.sort_values()

#%%
frame=pd.DataFrame({'b':[4,7,-3,2],'a':[0,1,0,1]})
frame

#%%
frame.sort_values(by='b')

#%%
frame.sort_values(by=['a','b'])

#%%
obj=pd.Series([7,-5,7,4,2,0,4])
obj.rank()

#%%
obj.rank(method='first')

#%%
obj.rank(ascending=False,method='max')

#%%
frame=pd.DataFrame({'b':[4.3,7,-3,2],'a':[0,1,0,1],'c':[-2,5,8,-2.5]})
frame

#%%
frame.rank(axis='columns')

#%%
# ##带有重复标签的轴索引
obj=pd.Series(range(5),index=['a','a','b','b','c'])
obj

#%%
obj.index.is_unique

#%%
obj['a']

#%%
obj['c']

#%%
df=pd.DataFrame(np.random.randn(4,3),index=['a','a','b','b'])
df

#%%
# 3.汇总和计算描述统计
df=pd.DataFrame([[1.4,np.nan],[7.1,-4.5],[np.nan,np.nan],[0.75,-1.3]],index=['a','b','c','d'],columns=['one','two'])
df

#%%
df.sum()

#%%
df.sum(axis=1)

#%%
# NA值会自动被排除，除非整个切片都是NA，通过skipna选项可以禁用该功能
df.mean(axis='columns',skipna=False)

#%%
df.idxmax()

#%%
df.cumsum()

#%%
df.describe()

#%%
obj=pd.Series(['a','a','b','c']*4)
obj.describe()

#%%
# ##相关系数与协方差
import pandas_datareader.data as web
all_data={ticker:web.get_data_yahoo(ticker) for ticker in ['AAPL','IBM','MSFT','GOOG']}
price=pd.DataFrame({ticker:data['Adj Close'] for ticker,data in all_data.item()})
volume=pd.DataFrame({ticker:data['Volume'] for ticker,data in all_data.items()})
returns=price.pct_change()
returns.tail()

#%%
