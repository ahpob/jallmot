import telegram
import requests,json,schedule,time


token = '5642908629:AAHBCZDc_IvIbt7UoOXupehtBfi-yDil5Ko'
id = "5241722694"
 
bot = telegram.Bot(token)
url = 'https://front.wemakeprice.com/api/wmpsuggest/hotkeyword/all.json'
headers = {
            'Referer': 'ticket.melon.com',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.70'
}

res = requests.get(url, headers=headers)
main_data=res.json()

before = list(map(lambda x: (x['rank'],x['keyword']),main_data['hits']))

def king() :
    bot.sendMessage(chat_id=id, text=before)


schedule.every(5).seconds.do(king)
    
# # step4.스캐쥴 시작
while True:
   schedule.run_pending()
   time.sleep(1)
# #print("Time elapsed: ", end - start)  # seconds  #-- 실행속도
# #print("Time elapsed: ", timedelta(seconds=end-start))  #-- 실행속도
