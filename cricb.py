import requests
from bs4 import BeautifulSoup
r=requests.get("https://www.cricbuzz.com/cricket-stats/icc-rankings")
c=r.content
#print(c)
soup=BeautifulSoup(c,"html.parser")
#print(soup)

teams=soup.find(id="teams-tests")
test_item=teams.find_all("div",{"class":"cb-col cb-col-100 cb-font-14 cb-brdr-thin-btm text-center"})
#print(test_item)


testteam=test_item[1]
#print(testteam.prettify())


list=[]
for i in test_item:
    d={}
    
    d["rank"]=i.find(class_="cb-col cb-col-20 cb-lst-itm-sm ").get_text()
    
    d["team"]=i.find(class_="cb-col cb-col-50 cb-lst-itm-sm text-left").get_text()
    d["rating"]=i.find(class_="cb-col cb-col-14 cb-lst-itm-sm").get_text()
    d["points"]=i.find(class_="cb-col cb-col-14 cb-lst-itm-sm ").get_text()
          
    
    #print(" ")
    #print(d)
    list.append(d)
#print(list)


import pandas
df=pandas.DataFrame(list)
print(df)

#df.to_csv("cricbuzz.csv")"""
