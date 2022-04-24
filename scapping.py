import requests
from bs4 import BeautifulSoup
url = "https://academics.mnnit.ac.in/new"

r = requests.get(url)
htmlContent = r.content
#print(htmlContent)


# Step 2: Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
mydivs = soup.find_all(id="notification-accordion")
#print(mydivs)


#mydivs = soup.find(id="notification-accordion")

file=open("New.txt","w")
for anu in mydivs:
    for item in anu.strings:
        print(item)
        file.write(item)
file.flush()
file.close