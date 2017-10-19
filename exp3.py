# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 20:43:38 2017

@author: wanglin
"""

import pandas as pd

inputfile = 'normalization_data.xls'
data = pd.read_excel(inputfile,header=None)#读取excel时，表格中第一行不是标题的情况不要把第一行当成标题
print(data)
print((data-data.min())/(data.max()-data.min()))
print((data-data.mean())/data.std())
print(data/1000)


