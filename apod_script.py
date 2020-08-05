from bs4 import BeautifulSoup as bs4
import requests
import time
from telegram import Bot
from datetime import datetime
import pytz

bot = Bot("1163369796:AAE1BI447fKiuDQ9RUTCUZKcS7-Ek96zlYI") #photobot

def get_url(page_text):
    if(page_text.find('img')):
        url = "https://apod.nasa.gov/apod/"+page_text.find_all('center')[0].find('img')['src']
        return(url)
    elif(page_text.find('iframe')):
        url = page_text.find_all('center')[0].find('iframe')['src']
        return url
        

while(True):
    url = "https://apod.nasa.gov/apod/astropix.html"
    response = requests.get(url)
    page_text = bs4(response.text, 'html.parser')
    
    old_response = requests.get(url)
    old_page_text = bs4(old_response.text, 'html.parser')
    old_date = old_page_text.find("p").contents[3].get_text().replace('\n','')
    #old_image_url = get_url(old_page_text)
    #old_title = old_page_text.find_all('center')[1].get_text().replace("\n","")

    #print(time.time())
    bot.sendMessage(chat_id="1045695336", text= "Going to sleep")
    time.sleep(30)
    
    new_response = requests.get(url)
    new_page_text = bs4(new_response.text, 'html.parser')
    new_date = new_page_text.find("p").contents[3].get_text().replace('\n','')
    new_image_url = get_url(new_page_text)
    new_title = new_page_text.find_all('center')[1].get_text().replace("\n","")
    new_explanation = new_page_text.find_all('p')[2].get_text().replace("\n","").split("Tomorrow")[0]


    if(old_date == new_date):
        bot.sendMessage(chat_id="1045695336", text= "no change")
        #bot.sendPhoto(chat_id="-1001331038106", photo=old_image_url, caption=str(old_title +"\nPicture taken on: " + old_date + "\n\n\ncourtesy of PhotoBot"))
        continue
    else:
        if(page_text.find('img')):
            bot.sendPhoto(chat_id="-1001284948052", photo=new_image_url, caption = str(new_title +"\nPicture taken on: " + new_date + "\n\n\ncourtesy of PhotoBot"))
        elif(page_text.find('iframe')):
            message = ("<a href=\""+new_image_url+"\">" +"<b>Astronomy Picture of the Day</b></a>\n\n" +"\n" +new_explanation+"\n<i>Date: "+new_date+"</i>\n")
            bot.sendMessage(chat_id="-1001284948052", text=message, parse_mode='HTML')
        bot.sendMessage(chat_id="-1001331038106", text= ("Updated at: " + str(datetime.now().astimezone(pytz.timezone('Asia/Kolkata')))))
        #bot.sendMessage()
        break
        
#def main():
#    #day = datetime.datetime.now().strftime("%A")
#    #time = int(datetime.datetime.now().strftime("%H"))
#    
#    updater = Updater('1183471904:AAENQORzTAU_mTDXfv8xJU1s3rmK1PuzlpU')
#    dp = updater.dispatcher
#    dp.add_handler(CommandHandler('wiki',get_wiki_info))
#    #dp.add_handler(MessageHandler(~Filters.command & Filters.text, test))
#    updater.start_polling()
#    updater.idle()
#
#if __name__ == '__main__':
#    main()
#