# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 18:18:19 2017

@author: wanglin
"""

import pandas as pd
from scipy.interpolate import lagrange

inputfile = 'catering_sale_all.xls'
outputfile= 'catering_sale_all.xls'

data = pd.read_excel(inputfile)#读取excel

def ployinterp_column(s,n,k=3):
    y=s[list(range(n-k,n))+list(range(n+1,n+1+k))]#取数，n的前后3个，这里有可能取到不存在的下标，为空
    y=y[y.notnull()]#如果y里面有空值的话就去掉
    print(list(y))
    return lagrange(y.index,list(y))(n)#最后的括号就是我们要插值的n  
for i in data.columns:
    if i==u'日期':
        continue
    for j in range(len(data)):
        try:#进行int转换，失败的时候表示为空或者为其它类型（包括空格）进行插值
            int(data[i][j])
        except ValueError:
            data[i][j] = round(ployinterp_column(data[i],j),1)
            
data.to_excel(outputfile,index=False)


#相关系数计算
print(data.corr()) #相关系数矩阵，即给出了任意两款菜式之间的相关系数
print(data.corr()[u'百合酱蒸凤爪'] )#只显示“百合酱蒸凤爪”与其他菜式的相关系数
print(data[u'百合酱蒸凤爪'].corr(data[u'翡翠蒸香茜饺'])) #计算“百合酱蒸凤爪”与“翡翠蒸香茜饺”的相关系数