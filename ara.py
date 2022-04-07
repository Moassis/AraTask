from distutils.log import error
from flask import Flask, request, json, jsonify
import pandas as pd
import requests
from bs4 import BeautifulSoup
app=Flask(__name__)

link1="https://www.swiggy.com/restaurants/gupta-grocery-store-gomti-nagar-lucknow-265502"
r1= requests.get(link1).content
soup1=BeautifulSoup(r1,'html.parser')
products=soup1.find_all('div', attrs={'class':'_2wg_t'})

string1=""
data=[]
for x in range(100):
    try:
        product=products[x].find('h3').text
    except:
        break
    string1=string1+product+", "
    data.insert(100,[product])
    
    
df=pd.DataFrame(data, columns=['Product_Name'])
df.to_excel('product.xlsx')
print("sucess")


@app.route('/')
def API_View():
    return(string1)


if(__name__=="__main__"):
    app.run(debug=True)
