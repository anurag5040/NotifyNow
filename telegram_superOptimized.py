import requests
import datetime

today = datetime.datetime.now()
files={'document':open('output.txt','rb')}
resp = requests.post('https://api.telegram.org/bot5304578747:AAFIVPBgUPaooZAs8bMLID_GKTtoryrwBqI/sendDocument?chat_id=1128822500&caption={}'.format(today), files=files)
print(resp.status_code)