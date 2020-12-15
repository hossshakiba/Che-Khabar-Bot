from telegram.ext import Updater, callbackcontext
from telegram.chataction import ChatAction
from data import *

sekke_price = sekke_price()

def bahar(update: Updater, context: callbackcontext):

    chat_id = update.message.chat_id
    context.bot.send_chat_action(chat_id, ChatAction.TYPING)
    update.message.reply_text(f'''
    #سکهـبهارـآزادی\n
    قیمت زنده : {sekke_price['bahar'][0].text} ریال
    
    کمترین قیمت روز : {sekke_price['bahar'][2].text} ریال
    
    بیشترین قیمت روز :‌ {sekke_price['bahar'][3].text} ریال
    
    آخرین ساعت به روز رسانی : {sekke_price['bahar'][4].text}
    ''')

def emami(update: Updater, context: callbackcontext):

    chat_id = update.message.chat_id
    context.bot.send_chat_action(chat_id, ChatAction.TYPING)
    update.message.reply_text(f'''
    #سکهـامامی\n
    قیمت زنده : {sekke_price['emami'][0].text} ریال
    
    کمترین قیمت روز : {sekke_price['emami'][2].text} ریال
    
    بیشترین قیمت روز :‌ {sekke_price['emami'][3].text} ریال
    
    آخرین ساعت به روز رسانی : {sekke_price['emami'][4].text}
    ''')

def nim(update: Updater, context: callbackcontext):

    chat_id = update.message.chat_id
    context.bot.send_chat_action(chat_id, ChatAction.TYPING)
    update.message.reply_text(f'''
    #نیمـسکه\n
    قیمت زنده : {sekke_price['nim'][0].text} ریال
    
    کمترین قیمت روز : {sekke_price['nim'][2].text} ریال
    
    بیشترین قیمت روز :‌ {sekke_price['nim'][3].text} ریال
    
    آخرین ساعت به روز رسانی : {sekke_price['nim'][4].text}
    ''')

def rob(update: Updater, context: callbackcontext):

    chat_id = update.message.chat_id
    context.bot.send_chat_action(chat_id, ChatAction.TYPING)
    update.message.reply_text(f'''
    #ربعـسکه\n
    قیمت زنده : {sekke_price['rob'][0].text} ریال
    
    کمترین قیمت روز : {sekke_price['rob'][2].text} ریال
    
    بیشترین قیمت روز :‌ {sekke_price['rob'][3].text} ریال
    
    آخرین ساعت به روز رسانی : {sekke_price['rob'][4].text}
    ''')
