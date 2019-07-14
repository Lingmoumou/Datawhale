#%% [markdown]
# # 这十套练习，教你如何用Pandas做数据分析, 
# > 数据集是科赛网出品的DATA TRAIN | 金融行业数据算法练习赛教程中对应的习题数据集，旨在通过串联一系列小数据集并附以代码分析的形式让读者对如何做数据分析进行更进一步的理解。
# > https://www.kesci.com/home/project/59e77a636d213335f38daec2
# | 习题编号 | 内容 | 相应数据集 |
# |练习1 - 开始了解你的数据 | 探索Chipotle快餐数据 | chipotle.tsv |
# |练习2 - 数据过滤与排序 | 探索2012欧洲杯数据 | Euro2012_stats.csv |
# |练习3 - 数据分组 | 探索酒类消费数据 | drinks.csv |
# |练习4 -Apply函数 | 探索1960 - 2014 美国犯罪数据 | US_Crime_Rates_1960_2014.csv |
# |练习5 - 合并 | 探索虚拟姓名数据 | 练习中手动内置的数据 |
# |练习6 - 统计 | 探索风速数据 | wind.data |
# |练习7 - 可视化 | 探索泰坦尼克灾难数据 | train.csv |
# |练习8 - 创建数据框 | 探索Pokemon数据 | 练习中手动内置的数据 |
# |练习9 - 时间序列 | 探索Apple公司股价数据 | Apple_stock.csv |
# |练习10 - 删除数据 | 探索Iris纸鸢花数据 | iris.csv |

# ## 练习1-开始了解你的数据
# > 探索Chipotle快餐数据
import pandas as pd
chipotle="../exercise_data/chipotle.tsv"
chipo=pd.read_csv(chipotle,sep='\t')
chipo.head(10)

#%%
chipo.shape[1] # 数据集中有多少个列(columns)

#%%
chipo.columns

#%%
chipo.index

#%%
# 被下单数最多商品(item)是什么?
c = chipo[['item_name','quantity']].groupby(['item_name'],as_index=False).agg({'quantity':sum})
c.sort_values(['quantity'],ascending=False,inplace=True)
c.head()

#%%
#在item_name这一列中，一共有多少种商品被下单？
chipo['item_name'].nunique()

#%%
# 在choice_description中，下单次数最多的商品是什么？
chipo['choice_description'].value_counts().head()

#%%
# 一共有多少商品被下单？
total_items_orders = chipo['quantity'].sum()

dollarizer = lambda x: float(x[1:-1]) # 将item_price转换为浮点数
chipo['item_price'] = chipo['item_price'].apply(dollarizer)
chipo['sub_total'] = round(chipo['item_price'] * chipo['quantity'],2)
chipo['sub_total'].sum() # 在该数据集对应的时期内，收入(revenue)是多少

#%%
# 在该数据集对应的时期内，一共有多少订单？
chipo['order_id'].nunique()

#%%
# 每一单(order)对应的平均总价是多少？
chipo[['order_id','sub_total']].groupby(by=['order_id']
).agg({'sub_total':'sum'})['sub_total'].mean()

# 一共有多少种不同的商品被售出
chipo['item_name'].nunique()