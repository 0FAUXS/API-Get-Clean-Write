#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 13:26:09 2024

@author: Lumin
@author: 0FAUXS
"""


import os
import pandas as pd
import tradermade as tm
import matplotlib.pyplot as plt

#Set the rest API key:
#https://tradermade.com
tm.set_rest_api_key("OGDUkhnf0DePHC-9nObb")
api_key = "OGDUkhnf0DePHC-9nObb"


#Get the list of currency from the API, serves two purposes, [1] if you need to know the currency code for your trading pair, [2] you have established that the connection and transfer of data is working. 
currencyDF = tm.currency_list()
with pd.option_context('display.max_rows', None,
                       'display.max_columns', None):
    print(currencyDF)

#getCurrencyPairDFs will print the information format that you are getting from this API. Sometimes it delivers all class 'pandas.core.frame.DataFrame' which is great, and some currency pairs will return a dictionary. It's best to know now. 
def getCurrencyPairDFs(currencyPairList, S, E):
    pairDFList = []
    nameList = []
    for sd,ed in zip(S, E):
        for cp in currencyPairList:
            start = f"{sd}-01-01"
            end = f"{ed}-12-31"
            
            data = tm.timeseries(currency=cp, start=start,end=end,interval="daily",fields=["close"]) 
            print(type(data))
            name = f"{cp}{ed}"
            data["name"] = name
            pairDFList.append(data)
            nameList.append(name)

    return pairDFList,nameList

def main(): 
    global pairDFList, nameList
    userCPinput = input("Enter comma-separated currency pairs: ").strip()
    externalCPList = userCPinput.split(',')
   
    userStart = int(input("What year do you want to start with? "))
    userEnd = int(input("What year do you want to end with? "))
    startRange = range(userStart, userEnd + 1)
    endRange = range(userStart, userEnd + 1)

    pairDFList, nameList = getCurrencyPairDFs(externalCPList, startRange, endRange)
  
if __name__=="__main__":    
    main()
    
#Check it...always
print(len(pairDFList), len(nameList))
print(nameList)


AUDUSDdf = pd.concat(pairDFList) 
AUDUSDdf = AUDUSDdf.drop_duplicates()
AUDUSDdf.set_index('date', inplace=True)
AUDUSDdf.index = pd.to_datetime(AUDUSDdf.index)
AUDUSDdf.head()

print(AUDUSDdf.index.dtype)
AUDUSDdf.dropna(inplace=True)
AUDUSDdf.info()

AUDUSDdf.plot(kind='line')
plt.title("First Look at AUDUSD")
plt.xticks(rotation=45)

pathFOREX = '/Users/Lumin/Desktop/4449 Capstone/FOREX data'
os.makedirs(pathFOREX, exist_ok = True)
fp = os.path.join(pathFOREX, "AUDUSDdf19_23.csv")
AUDUSDdf.to_csv(fp)