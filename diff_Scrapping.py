import requests


from bs4 import BeautifulSoup

soup = BeautifulSoup(open('difference_report.html'),'html.parser')

file=open("Output.txt","w")

a=soup.find_all("span", class_="diff_add")
for i in a :
     for item in i.strings:
         print(item)
         file.write(item)
file.flush()
file.close