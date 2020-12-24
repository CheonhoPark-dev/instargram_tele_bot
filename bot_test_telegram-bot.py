#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from telegram.ext import Updater, MessageHandler, Filters, CommandHandler  # import modules

my_token = '1413710762:AAGdp_PDSMwvh-PY4PI9nF_GG0H-L_Ocr4g'

print('start telegram chat bot')


# message reply function
def get_message(update, context) :
    update.message.reply_text("got text")
    update.message.reply_text(update.message.text)


# help reply function
def help_command(update, context) :
    update.message.reply_text("무엇을 도와드릴까요?")


updater = Updater(my_token, use_context=True)

message_handler = MessageHandler(Filters.text & (~Filters.command), get_message) # 메세지중에서 command 제외
updater.dispatcher.add_handler(message_handler)

help_handler = CommandHandler("help", help_command)
updater.dispatcher.add_handler(help_handler)

updater.start_polling(timeout=3, clean=True)
updater.idle()


# In[ ]:


import telegram

my_token = '1413710762:AAGdp_PDSMwvh-PY4PI9nF_GG0H-L_Ocr4g' #토큰을 설정해 줍니다.

bot = telegram.Bot(token = my_token) #봇을 생성합니다.

bot.sendMessage(chat_id='@bill_chat', text="I'm bot") #@bill_chat 으로 메세지를 보냅니다.


# In[4]:


import telegram   #텔레그램 모듈을 가져옵니다.

my_token = '1413710762:AAGdp_PDSMwvh-PY4PI9nF_GG0H-L_Ocr4g'   #토큰을 변수에 저장합니다.

bot = telegram.Bot(token = my_token)   #bot을 선언합니다.

updates = bot.getUpdates()  #업데이트 내역을 받아옵니다.

for u in updates :   # 내역중 메세지를 출력합니다.
    print(u.message)
    
chat_id = bot.getUpdates()[-1].message.chat.id #가장 최근에 온 메세지의 chat id를 가져옵니다

bot.sendMessage(chat_id = chat_id, text="저는 봇입니다.")


# In[ ]:




