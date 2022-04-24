from alive import alive
import os
import difflib
import requests
from bs4 import BeautifulSoup
import datetime
import telepot
import time

alive()
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
        # print(item)
        file.write(item)
file.flush()
file.close

#giving the paths for various required files.....
HOME_DIR = os.path.abspath(os.pardir)

Oldpath = "Old.txt"
Newpath = "New.txt"

# if os.path.exists(Oldpath) and os.path.exists(Newpath):
#     print("Success!!!!!")

OldFileObj = open(Oldpath, mode='r')
NewFileObj = open(Newpath, mode='r')

#logic to split and arrange/list content for comparision.....
OldList = OldFileObj.read().split('\n')
NewList = NewFileObj.read().split('\n')

#sorting(ascending by default) for compairing and detecting changes.....
OldList.sort()
NewList.sort()

#Building logic to detect any changes over webpage content to use as further code execution condition......
if NewList == OldList:
  print("Same!!!!!")

else:
  print("Not Same!!!!!")
  
# if condition to detect any changes on MNNIT website notification container in order to execute furter functionality commented below......
if OldList != NewList:
    first_file = "Old.txt"
    second_file = "New.txt"
  
# Generating HTML file with spotted changes within notifications.....
    first_file_lines = open(first_file).readlines()
    second_file_lines = open(second_file).readlines()
    difference = difflib.HtmlDiff().make_file(first_file_lines,
                                              second_file_lines, first_file,
                                              second_file)
    difference_report = open('difference_report.html', 'w')
    difference_report.write(difference)
    difference_report.close()

  #Code to clear previous content of Old.txt with New.txt when changes detects for future comparison.....
    file_to_read = "New.txt"
    write_to_file = "Old.txt"
    file = open(file_to_read, "r")
    data = file.read()
    file.close() 
    with open(write_to_file, "a") as file:
        f = open('Old.txt', 'r+')
        f.truncate(0)
        file.write(data)
    print('completed')
  
  # Scrapping Code for saved/updated difference_report HTML file.......
    soup = BeautifulSoup(open('difference_report.html'), 'html.parser')
    file = open("Output.txt", "w")
    a = soup.find_all("span", class_="diff_add")
    for i in a:
        for item in i.strings:
            print(item)
            file.write(item)
    file.flush()
    file.close
    
# Telegram_Bot feature added here...............
    today = datetime.datetime.now()
    files={'document':open('Output.txt','rb')}
    resp = requests.post('https://api.telegram.org/bot5304578747:AAFIVPBgUPaooZAs8bMLID_GKTtoryrwBqI/sendDocument?chat_id=1128822500&caption={}'.format(today), files=files)
    print(resp.status_code)

#Backup stuff.....
    # lines = []
    # with open('Output.txt') as f:
    #  lines = f.readlines()
  
    # token = '5304578747:AAFIVPBgUPaooZAs8bMLID_GKTtoryrwBqI' 
    # receiver_id = 1128822500


    # bot = telepot.Bot(token)

    # bot.sendMessage(receiver_id, lines) 

