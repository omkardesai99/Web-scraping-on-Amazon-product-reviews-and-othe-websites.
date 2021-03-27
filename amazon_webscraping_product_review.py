import pandas as pd
import requests
from bs4 import BeautifulSoup

z=0
z={}
amazon=pd.DataFrame(z)
headline=0
articlebody=0
headline=[]
articlebody=[]
urls=[]
u='https://www.amazon.in/OnePlus-Nord-Gray-128GB-Storage/product-reviews/B08695ZSP6/ref=cm_cr_getr_d_paging_btm_prev_1?ie=UTF8&reviewerType=all_reviews&pageNumber='

for i in range(1,21):    
    i=str(i)
    a=u+i  
    urls.append(a)

print(urls)
for i in urls:
    data = requests.get(i)
    data.content
    #or
    #data.text
    soup=BeautifulSoup(data.content,'html.parser')
    soup
    soup.title
    soup.head
    title=soup.find_all('a',{'data-hook':"review-title"},class_=["a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold"])
    #title.find('span',attrs={'itemprop':'headline'}).string
    title
    for i in title:       
        headline.append(i.find('span').text)
            #'a',class_=["a-size-base a-link-normal review-title a-color-base review-title-content a-text-bold"]))
        #headline.extend([headline1])
    headline
    
    body=soup.find_all('span', {'data-hook':"review-body"}, class_=["a-size-base review-text review-text-content"])
    body
    #body[0].find('div',attrs={"itemprop":"articleBody"}).string  
    for i in body:
        articlebody.append(i.find('span').text)
        #articlebody.extend([articlebody1])
        articlebody
        
    

amazon['headline']=headline
amazon['articlebody']=articlebody
    


amazon.to_csv(r'C:\Users\omkar desai\Desktop\Artificial Inteligence\amazon11.csv')
    


















































































