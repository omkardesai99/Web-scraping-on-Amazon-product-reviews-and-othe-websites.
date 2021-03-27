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
    


        
        
        
        
        
        
        


'''
Headline=[]
for i in headline:
    Headline.extend([headline[i]])

Articlebody=[]
for i in headline:
    Articlebody.extend([articlebody[i]])
'''




























url='https://www.inshorts.com/en/read/technology'
data = requests.get(url)
data.content
#or
#data.text
soup=BeautifulSoup(data.content,'html.parser')
soup
soup.title
title1=soup.find_all('div',class_=["news-card-title news-right-box"])
title1[0].find('span',attrs={'itemprop':'headline'}).string   #find is to only find one line''' not many rows i list''' as obsrved
headline1=[]
for i in title1:
    headline1.append(i.find('span',attrs={'itemprop':'headline'}).string)
    
headline1

body1=soup.find_all('div',class_=["news-card-content news-right-box"])
body1[0].find('div',attrs={"itemprop":"articleBody"}).string
articlebody1=[]
for i in body1:
    articlebody1.append(i.find('div',attrs={"itemprop":"articleBody"}).string)

len(articlebody1)
articlebody1

#sports****************************************************************
url='https://www.inshorts.com/en/read/sports'
data = requests.get(url)
data.content
#or
#data.text
soup=BeautifulSoup(data.content,'html.parser')
soup
soup.title
title2=soup.find_all('div',class_=["news-card-title news-right-box"])
title2[0].find('span',attrs={'itemprop':"headline"}).string
headline2=[]
for i in title2:
    headline2.append(i.find('span',attrs={'itemprop':'headline'}).string)
    
headline2

body2=soup.find_all('div',class_=["news-card-content news-right-box"])
body2[0].find('div',attrs={'itemprop':"articleBody"}).string
articlebody2=[]
for i in body2:
    articlebody2.append(i.find('div',attrs={"itemprop":"articleBody"}).string)

len(articlebody2)
articlebody2



#politis
url='https://www.inshorts.com/en/read/politics'
data = requests.get(url)
data.content
#or
#data.text
soup=BeautifulSoup(data.content,'html.parser')
soup
soup.title
title3=soup.find_all('div',class_=["news-card-title news-right-box"])
title3[0].find('span',attrs={"itemprop":"headline"}).string
headline3=[]
for i in title3:
    headline3.append(i.find('span',attrs={'itemprop':'headline'}).string)
    
headline3

body3=soup.find_all('div',class_=["news-card-content news-right-box"])
body3[0].find('div',attrs={'itemprop':"articleBody"}).string
articlebody3=[]
for i in body3:
    articlebody3.append(i.find('div',attrs={"itemprop":"articleBody"}).string)

len(articlebody3)
articlebody3


#b={headline1:articlebody1,headline2:articlebody2,headline3:articlebody3}

title=[]
title.extend([headline1,headline2,headline3])
title
articlebody=[]
articlebody.extend([articlebody1,articlebody2,articlebody3])

dict1={'title':title,'articlebody':articlebody}
dict1
df=pd.DataFrame(dict1)
df



































































