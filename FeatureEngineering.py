# -*- coding: utf-8 -*-
"""
Created on Sun May 16 20:55:58 2021

@author: bornf
"""
import pandas as pd
import sklearn.metrics as sk
import scipy.stats as sc

# Replacing NaN with 0 and dropping any constant columns
def dropConst(df):
    n = df.shape[0]
    for i in range(25,n-1,26): # Because of how the HTML is on the page, got to clean it up like this
        df.drop(labels=i,axis=0,inplace=True)
    headers_init = []
    headers_final = []
    for i in df.keys():
        headers_init.append(list(i))
        
    for i in headers_init:
        del i[0]
        i = str(i[0])
        headers_final.append(i)
        
    df.columns=headers_final
    df = df.loc[:, (df != df.iloc[0]).any()]
    df.fillna(0, inplace=True)
    return df

# Defining the data entry of the target player

def targetPlayer(df, name):    
    
    val = df.loc[df['Player'] == name]
    return val

def main():
    url = "https://fbref.com/en/comps/Big5/stats/players/Big-5-European-Leagues-Stats"
    dfOverall = pd.read_html(url, attrs={"id": "stats_standard"})[0]
    print(dfOverall)
    
    
if __name__ == "__main__":
    main()