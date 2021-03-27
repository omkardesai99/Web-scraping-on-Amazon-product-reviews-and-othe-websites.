import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import nltk
from nltk.tokenize import RegexpTokenizer
import os
import requests
from bs4 import BeautifulSoup

import re
import string

urls=['https://inshorts.com/en/read/sports','https://inshorts.com/en/read/politics','https://inshorts.com/en/read/technology']
s=0
s={}
web=pd.DataFrame(s)
category=0
headline=0
articlebody=0
category=[]
headline=[]
articlebody=[]
for i in urls:
    cat=i.split('/')[-1]

    data = requests.get(i)
    data.content
    #or
    #data.text
    soup=BeautifulSoup(data.content,'html.parser')
    soup
    soup.title
    title=soup.find_all('div',class_=["news-card-title news-right-box"])
    #title.find('span',attrs={'itemprop':'headline'}).string
       
    for i in title:       
        headline.append(i.find('span',attrs={'itemprop':'headline'}).string) 
        #headline.extend([headline1])
        category.append(cat)
    headline
    
    body=soup.find_all('div',class_=["news-card-content news-right-box"])
    #body[0].find('div',attrs={"itemprop":"articleBody"}).string  
    for i in body:
        articlebody.append(i.find('div',attrs={"itemprop":"articleBody"}).string)
        #articlebody.extend([articlebody1])
        articlebody
        
    
web['category']=category
web['headline']=headline
web['articlebody']=articlebody
    


web.to_csv(r'C:\Users\omkar desai\Desktop\Artificial Inteligence\websearch6.csv')
    

