# -*- coding: utf-8 -*-
"""Prices3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1YjBiVdez81qdIwINr_sbjAQl1fpCJt4e
"""

import numpy as np
import pandas as pd

df = pd.read_excel("Prices3.xlsx")

df.head()

da = df.Date.unique()

new_dic={}
flag=True
for i in da:
  df1 = df[df.Date==i]
  a=[i.month for i in df1["Contract Month"]]
  b=[i.year for i in df1["Contract Month"]]
  c=len(a)
  hh=[]
  for w in range(0,c):
    g=(a[w],b[w])
    hh.append(g)
  df1["Month"]=hh
  df2=pd.DataFrame({"Month":hh})
  a=pd.merge(df2,df1.loc[:,["Month","Price"]],how="outer")
  ddf=pd.DataFrame({"Month":a.Month,"Price":a.Price})
  new_dic[i]=ddf

final_df=pd.DataFrame({"Month":[]})
for a in da:
  final_df=pd.merge(final_df,new_dic[a],on="Month",how="outer")

da=list(da)
da.insert(0,"Month")

final_df.columns=da

vs=[]
for a in final_df["Month"]:
  vs.append(pd.to_datetime(str(a[1])+"-"  + str(a[0])))

final_df["Month1"]=vs

final_df=final_df.T
final_df=final_df.sort_values(by="Month1")

final_df=final_df.T
final_df.drop(labels=["Month","Month1"],axis=0,inplace=True)
final_df

final_df.fillna(method="ffill",axis=0,inplace=True)

final_df

final_df.to_excel("Final.xlsx")