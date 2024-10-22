# -*- coding: utf-8 -*-
"""
Created on Mon May 17 12:41:48 2021

@author: bornf
"""

import pandas as pd
import numpy as np
import sklearn.metrics as sk
import scipy.stats as sc


def simCalc(df, target, name):
    test_df_temp = df.copy()
    test_df_temp.drop(columns=test_df_temp.columns[:8], axis=1, inplace=True)
    test_df_temp = test_df_temp.apply(pd.to_numeric)
    test_df = test_df_temp[test_df_temp['90s'] >= 10]
    test_target = target.copy()
    test_target.drop(columns=test_target.columns[:8], axis=1, inplace=True)
    target_array = np.array(test_target.values.tolist()[0], dtype=float)
    n = test_df.shape[0]
    cos_values = []
    temp = test_df.drop(test_df.std()[test_df.std() < 0.4].index.values, axis=1)
    test_target = test_target[temp.keys()]
    test_df = test_df[temp.keys()]
    # print(test_target)
    # print(test_df)
    # print(temp)
    # print()
    #print(temp)
    for i in range(n):
        cos = sk.pairwise.cosine_similarity(test_df[i:i+1], test_target)
        cos_values.append(cos)
    test_df['Cosine Similarity'] = cos_values
    # print(sc.pearsonr(target_array,test_df))
    df.insert(df.shape[1],'Cosine Similarity', test_df['Cosine Similarity'])
    # print(df)
    # index_values = test_df.index.values
    # print(index_values)
    # print(len(index_values))
    # print(test_df)
    # count = 0
    # for i in index_values:
    #     df.iloc[i, df.columns.get_loc('Similarity')] = test_df.iloc[count]['Cosine Similarity']
    #     count+=1
    df = df.sort_values(by=['Cosine Similarity'], ascending =False)
    df = df[df.Player != name]
    df.drop(columns=['Rk'], inplace=True)
    return df
