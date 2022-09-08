import requests,os
import json,schedule,time

#디스코드 웹훅
from discord import SyncWebhook
discord_url = os.environ['Discord_Url']
webhook = SyncWebhook.from_url(discord_url)

# # 텔레그램봇
# token = os.environ['TELEGRAM_TOKEN']
# id = os.environ['TELEGRAM_ID']
# bot = telegram.Bot(token)

url = 'https://front.wemakeprice.com/api/wmpsuggest/hotkeyword/all.json'
headers = {
            'Referer': 'ticket.melon.com',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70'
}
res = requests.get(url, headers=headers)
main_data=res.json()['hits']

rank = []
for i in range(len(main_data)):
    a = main_data[i]['rank']
    rank.append((main_data[i]['rank'],main_data[i]["keyword"]))
        
   # print(rank)
    #real = list(int(main_data[i]['realseatCntlk']))
    #print(real)

    #result = list(filter(lambda x: x>0, real)
    #print(result)
    #list(filter(lambda x: x>0, int(main_data[i]['realseatCntlk'])))
    #print(main_data[i]['rank'])

def king() :
    webhook.send(rank)
  
schedule.every(10).seconds.do(king)
    
# # step4.스캐쥴 시작
while True:
    schedule.run_pending()
    time.sleep(1)
# #print("Time elapsed: ", end - start)  # seconds  #-- 실행속도
# #print("Time elapsed: ", timedelta(seconds=end-start))  #-- 실행속도
