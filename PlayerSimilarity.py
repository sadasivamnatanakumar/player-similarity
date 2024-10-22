# -*- coding: utf-8 -*-
"""
Created on Mon May  3 13:33:52 2021

@author: Sadasivam
"""

import pandas as pd
import sklearn.metrics as sk
import scipy.stats as sc
from FeatureEngineering import *
from SimilarityMetrics import *


"""Import the datasets containing the various
types of player attributes, clubbed by their actions on the field"""

# Preparing dataframes from the html pages

url1 = "https://fbref.com/en/comps/Big5/"
url2 = "/players/Big-5-European-Leagues-Stats"


shootingBaseData = pd.read_html(url1 + "shooting" + url2)[0]
passingBaseData = pd.read_html(url1 + "passing" + url2)[0]
passTypeBaseData = pd.read_html(url1 + "passing_types" + url2)[0]
creationBaseData = pd.read_html(url1 + "gca" + url2)[0]
defendingBaseData = pd.read_html(url1 + "defense" + url2)[0]
possessionBaseData = pd.read_html(url1 + "possession" + url2)[0]
miscellaneousBaseData = pd.read_html(url1 + "misc" +url2)[0]

# x = [156, 5, 112, 21, 3, 9,	8,	3,	26,	1,	22,	2,	0,	2,	0,	0,	0]
# y = [146, 5, 79, 43, 9,	6,	7,	2,	13,	0,	4,	5,	1,	2,	1,	0,	0]

# print(sk.pairwise.cosine_similarity((x,y)))
# print(sc.pearsonr(x,y))

# Replacing NaN with 0 and dropping any constant columns

shootingBaseData = dropConst(shootingBaseData)
passingBaseData = dropConst(passingBaseData)
passTypeBaseData = dropConst(passTypeBaseData)
creationBaseData = dropConst(creationBaseData)
defendingBaseData = dropConst(defendingBaseData)
possessionBaseData = dropConst(possessionBaseData)
miscellaneousBaseData = dropConst(miscellaneousBaseData)

# print(passingBaseData.head())
# print(passTypeBaseData.head())
# print(creationBaseData.head())
# print(defendingBaseData.head())
# print(possessionBaseData.head())
# print(miscellaneousBaseData.head())
name = 'Mohamed Salah'

shootingTargetRow = targetPlayer(shootingBaseData,name)
passingTargetRow = targetPlayer(passingBaseData, name)
passTypeTargetRow = targetPlayer(passTypeBaseData,name)
creationTargetRow = targetPlayer(creationBaseData,name)
defendingTargetRow = targetPlayer(defendingBaseData,name)
possessionTargetRow = targetPlayer(possessionBaseData,name)
misscellaneousTargetRow = targetPlayer(miscellaneousBaseData,name)


shootingFinalData = simCalc(shootingBaseData, shootingTargetRow, name)
passingFinalData = simCalc(passingBaseData, passingTargetRow, name)
passTypeFinalData = simCalc(passTypeBaseData, passTypeTargetRow, name)
creationFinalData = simCalc(creationBaseData, creationTargetRow, name)
defendingFinalData = simCalc(defendingBaseData, defendingTargetRow, name)
possessionFinalData = simCalc(possessionBaseData, possessionTargetRow, name)
miscellaneousFinalData = simCalc(miscellaneousBaseData, misscellaneousTargetRow, name)

writer = pd.ExcelWriter('C:/Users/bornf/Documents/Player Similarity Model/SimilarityFinal/'+ name + ' Similarity.xlsx')

shootingFinalData.to_excel(writer, sheet_name = 'Shooting', index = False)
passingFinalData.to_excel(writer, sheet_name = 'Passing', index = False)
passTypeFinalData.to_excel(writer, sheet_name = 'PassType', index = False)
creationFinalData.to_excel(writer, sheet_name = 'Creation', index = False)
defendingFinalData.to_excel(writer, sheet_name = 'Defending', index = False)
possessionFinalData.to_excel(writer, sheet_name = 'Possession', index = False)
miscellaneousFinalData.to_excel(writer, sheet_name = 'Miscellaneous', index = False)

writer.save()

