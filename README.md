# API-Get-Clean-Write
API call to https://tradermade.com for FOREX historical data
0FAUXS

GET it:

Set the rest API key:
#https://tradermade.com

Get the list of currency from the API, serves two purposes, [1] if you need to know the currency code for your trading pair, [2] you have established that the connection and transfer of data is working. 

getCurrencyPairDFs() will print the information format that you are getting from this API. Sometimes it delivers all class 'pandas.core.frame.DataFrame' which is great, and some currency pairs will return a dictionary. It's best to know now. 

CLEAN IT...always

WRITE IT...usually always;)

If you are loading one piece of information, then it is easy to keep straight. This function is a way to have data and write files using the API call itself to denote the name of your structures. This particular free API does require a log-in <easy> and you only get1000 retrievals per month, but for your project, I am guessing that will be fine. With development especially, writing to a file keep your API calls to a minimum. If you want to drop extra columns with the name of the data, great--do it!! But no matter how much information you have there is a way to sync it perfectly to reality, and that's nice.

Lumin
0FAUXS
