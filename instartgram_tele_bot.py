#!/usr/bin/env python
# coding: utf-8

# In[1]:


import telepot
import datetime
import time
import threading
import os

access_token = os.environ["BOT_TOKEN"]
token = access_token
mc = '367804458'
bot = telepot.Bot(token)


# In[2]:


global likerange
global followrange
global commentrange
global finishkey

likerange = 30
followrange = 30
commentrange = 30
finishkey = 0

def handle(msg):
    global finishkey
    global likerange
    global followrange
    global commentrange
    splitmsg = msg['text'].split()
    
    if splitmsg[0] == "/활동시작":
        if finishkey == 1:
            bot.sendMessage(msg['chat']['id'], "이미 누가 활동 중입니다.")
        else:
            bot.sendMessage(msg['chat']['id'], "{} 활동을 시작합니다!".format(splitmsg[1]))
            bot.sendMessage(msg['chat']['id'], "좋아요 가능 개수 : {}\n팔로우 가능 개수 : {}\n댓글 가능 개수 : {}"
                    .format(likerange, followrange, commentrange))
            finishkey = 1

    if splitmsg[0] == "/활동보고":
        if finishkey == 1:
            likereport = int(splitmsg[1])
            followreport = int(splitmsg[2])
            commentreport = int(splitmsg[3])
            
            bot.sendMessage(msg['chat']['id'], "활동을 보고합니다!")
            endtime = datetime.datetime.now()
            bot.sendMessage(msg['chat']['id'], "종료 시간 {}시 {}분 \n좋아요 수 : {}\n팔로우 수 : {}\n댓글 수 : {}\n\nMVP 점수 : {}"
                        .format(endtime.hour, endtime.minute, likereport, followreport, commentreport, 
                                int(likereport/15)+int(followreport/10)+int(commentreport/5)))
            finishkey = 0
            
            
            timep = threading.Thread(target=timepass, args=(endtime, likereport, followreport, commentreport))
            timep.start()
        else:
            bot.sendMessage(msg['chat']['id'], "활동 시작을 먼저 해주십시오.")
            
bot.message_loop(handle)


# In[3]:


def timepass(now_1, like, follow, comment):
    global likerange
    global followrange
    global commentrange
    
    hour_1 = now_1.hour
    min_1 = now_1.minute
    
    likerange = likerange - like
    followrange = followrange - follow
    commentrange = commentrange - comment
    
    while True:
        now_2 = datetime.datetime.now()
        hour_2 = now_2.hour
        min_2 = now_2.minute

        if (min_1 == min_2) and (hour_1 + 1 == hour_2):
            break
            
    likerange = likerange + like
    followrange = followrange + follow
    commentrange = commentrange + comment

