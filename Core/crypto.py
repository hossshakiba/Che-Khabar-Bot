from telegram.ext import Updater, callbackcontext
from telegram.chataction import ChatAction
from data import *

crypto = crypto()


def bitcoin(update: Updater, context: callbackcontext):

    chat_id = update.message.chat_id
    context.bot.send_chat_action(chat_id, ChatAction.TYPING)
    update.message.reply_text(f'''
    #بیتـکوین\n
    قیمت زنده : {crypto[0].text} دلار
    
    کمترین قیمت روز : {crypto[2].text} ریال
    
    بیشترین قیمت روز :‌ {crypto[3].text} ریال
    
    آخرین ساعت به روز رسانی : {crypto[4].text}
    ''')
def etherium(update: Updater, context: callbackcontext):

    chat_id = update.message.chat_id
    context.bot.send_chat_action(chat_id, ChatAction.TYPING)
    update.message.reply_text(f'''
    #اتریوم\n
    قیمت زنده : {crypto[5].text} دلار
    
    کمترین قیمت روز : {crypto[8].text} ریال
    
    بیشترین قیمت روز :‌ {crypto[9].text} ریال
    
    آخرین ساعت به روز رسانی : {crypto[10].text}
    ''')
def tether(update: Updater, context: callbackcontext):

    chat_id = update.message.chat_id
    context.bot.send_chat_action(chat_id, ChatAction.TYPING)
    update.message.reply_text(f'''
    #تتر\n
    قیمت زنده : {crypto[12].text} دلار
    
    کمترین قیمت روز : {crypto[14].text} ریال
    
    بیشترین قیمت روز :‌ {crypto[15].text} ریال
    
    آخرین ساعت به روز رسانی : {crypto[16].text}
    ''')
def dash(update: Updater, context: callbackcontext):

    chat_id = update.message.chat_id
    context.bot.send_chat_action(chat_id, ChatAction.TYPING)
    update.message.reply_text(f'''
    #دش\n
    قیمت زنده : {crypto[18].text} دلار
    
    کمترین قیمت روز : {crypto[20].text} ریال
    
    بیشترین قیمت روز :‌ {crypto[21].text} ریال
    
    آخرین ساعت به روز رسانی : {crypto[22].text}
    ''')
def riple(update: Updater, context: callbackcontext):

    chat_id = update.message.chat_id
    context.bot.send_chat_action(chat_id, ChatAction.TYPING)
    update.message.reply_text(f'''
    #ریپل\n
    قیمت زنده : {crypto[24].text} دلار
    
    کمترین قیمت روز : {crypto[26].text} ریال
    
    بیشترین قیمت روز :‌ {crypto[27].text} ریال
    
    آخرین ساعت به روز رسانی : {crypto[28].text}
    ''')
def litecoin(update: Updater, context: callbackcontext):

    chat_id = update.message.chat_id
    context.bot.send_chat_action(chat_id, ChatAction.TYPING)
    update.message.reply_text(f'''
    #ریپل\n
    قیمت زنده : {crypto[30].text} دلار
    
    کمترین قیمت روز : {crypto[32].text} ریال
    
    بیشترین قیمت روز :‌ {crypto[33].text} ریال
    
    آخرین ساعت به روز رسانی : {crypto[34].text}
    ''')