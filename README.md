# API-Get-Clean-Write
API call to https://tradermade.com for FOREX historical data
0FAUXS

GET it:

Set the rest API key:
#https://tradermade.com

Get the list of currency from the API, serves two purposes, [1] if you need to know the currency code for your trading pair, [2] you have established that the connection and transfer of data is working. 

getCurrencyPairDFs() will print the information format that you are getting from this API. Sometimes it delivers all class 'pandas.core.frame.DataFrame' which is great, and some currency pairs will return a dictionary. It's best to know now. 

Check it...always

Write it...usually always;)
