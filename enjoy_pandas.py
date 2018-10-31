# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np

if __name__=='__main__':

    
    '''
        name    age
    0   a       12
    1   b       20 
    2   c       30
    '''
    # 创建df表
    # df = pd.DataFrame([{'name':'a','age':12},
    #                    {'name': 'b', 'age': 20},
    #                    {'name': 'c', 'age': 30}])
    df = pd.DataFrame({'name':['a','b','c'],'age':[12,20,30]})
    df2 = pd.DataFrame({'name':['a','b','c'],'age':[12,20,30]},index=['aa','bb','cc'])
    df3 = pd.DataFrame({'AAA':[1,1,1,2,2,2,3,3],'BBB':[2,1,3,4,5,1,2,3]})

    # 列数=>2
    print(df.shape[1])
    print(df.columns.size)
    print(len(df.columns))
    # 行数=>3
    print(df.shape[0])
    print(len(df.index))
    print(len(df))
    # 大小=>(3, 2)
    print(df.shape)
    # 列名=>['name','age']
    print(df.columns.tolist())
    print(list(df))
    # 索引名=>[0,1,2]
    print(df.index.tolist())


    # 前2行
    print(df.head(2))
    # 后2行
    print(df.tail(2))
    # 行列互换
    print(df.T)
    # 列类型
    print(df.dtypes)
    # 空?
    print(df.empty)


    # 取name列=>Series
    print(df['name'])
    # 取name列=>DataFrame
    print(df[['name']])
    # 添加列
    df['addr']=['HZ','SH','BJ']


    '''
    where
    '''
    # 选择age>=20,实现if-then逻辑
    print(df.ix[df.age>=20])
    print(df.ix[df.age>=20,['name']])
    print(df.where(df.age>=20))
    print(df[df.age>=20])
    # 重新赋值
    df.ix[df.age>=20,['name']]='dd'
    # 添加新列,实现if-then-else逻辑
    df['tt'] = np.where(df.age>=20,'true','false')
    # 查询and
    print(df.loc[(df.age>10) & (df.age<30)])
    # 查询or
    print(df.loc[(df.age<10) | (df.age>25)])
    # 修改
    df.loc[(df.age<10) | (df.age>25)]=['tt',40,'tt','tt']
    # 选择age>=20,实现if-then逻辑,取相应行
    print(df[(df.age>20)&(df.index.isin([0,2]))])
    # 取反向
    print(df[~(df.age>=20)])

    '''
    切片
    '''
    # 下标导向(不包含右侧值)
    print(df2.ix[0:2])
    # 索引名导向(包含右侧值)
    print(df2.loc['aa':'cc'])
    print(df2.ix['aa':'cc'])

    '''
    groupby
    '''
    # 获取分组中最小值
    print(df3.loc[df3.groupby('AAA')['BBB'].idxmin()])
    print(df3.sort_values(by="BBB").groupby("AAA", as_index=False).first())

    

