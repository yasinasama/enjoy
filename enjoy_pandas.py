# -*- coding: utf-8 -*-

import pandas as pd

if __name__=='__main__':
    df = pd.DataFrame([{'name':'a','age':12},
                       {'name': 'b', 'age': 20},
                       {'name': 'c', 'age': 30}])

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
