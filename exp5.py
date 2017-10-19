# -*- coding: utf-8 -*-
"""
Created on Wed Oct 11 22:46:46 2017

@author: wanglin
"""

import pandas as pd

inputfile = 'sales_data.xls'
outputfile= 'data_tras.xls'
data = pd.read_excel(inputfile) #读取数据  
#print(data)#调试代码
size_mapping = {  
           '好': 0,  
           '坏': 1, 
           '是': 0, 
           '否': 1, 
           '高': 0,  
           '低': 1}  
data['天气'] = data['天气'].map(size_mapping) 
data['是否周末'] = data['是否周末'].map(size_mapping) 
data['是否有促销'] = data['是否有促销'].map(size_mapping) 
data['销量'] = data['销量'].map(size_mapping) 
#print(data)#调试代码
data.to_excel(outputfile,index=False)



