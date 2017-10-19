# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 22:46:46 2017

@author: wanglin
"""

import pandas as pd

inputfile = 'discretization_data.xls'
outputfile= 'data_descret.xls'
data = pd.read_excel(inputfile) #读取数据  
#print(data)
data = data[u'肝气郁结症型系数']
k = 4  
d1 = pd.cut(data, k, labels = range(k)) #等宽离散化，各个类比依次命名为0,1,2,3   
#print(d1)#调试代码
d1.to_excel(outputfile,index=False)