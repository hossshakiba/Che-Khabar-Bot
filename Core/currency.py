from telegram.ext import Updater, callbackcontext
from telegram.chataction import ChatAction
from data import arz_price

arz_price = arz_price()

def dollar_usa(update: Updater, context: callbackcontext):

    chat_id = update.message.chat_id
    context.bot.send_chat_action(chat_id, ChatAction.TYPING)
    update.message.reply_text(f'''
    #دلارـآمریکا\n
    قیمت زنده : {arz_price['dollar_usa'][0].text} ریال
    
    کمترین قیمت روز : {arz_price['dollar_usa'][2].text} ریال
    
    بیشترین قیمت روز :‌ {arz_price['dollar_usa'][3].text} ریال
    
    آخرین ساعت به روز رسانی : {arz_price['dollar_usa'][4].text}
    ''')
def euro(update: Updater, context: callbackcontext):

    chat_id = update.message.chat_id
    context.bot.send_chat_action(chat_id, ChatAction.TYPING)
    update.message.reply_text(f'''
    #یورو\n
    قیمت زنده : {arz_price['euro'][0].text} ریال
    
    کمترین قیمت روز : {arz_price['euro'][2].text} ریال
    
    بیشترین قیمت روز :‌ {arz_price['euro'][3].text} ریال
    
    آخرین ساعت به روز رسانی : {arz_price['euro'][4].text}
    ''')

def pond(update: Updater, context: callbackcontext):

    chat_id = update.message.chat_id
    context.bot.send_chat_action(chat_id, ChatAction.TYPING)
    update.message.reply_text(f'''
    #پوندـانگلیس\n
    قیمت زنده : {arz_price['pond'][0].text} ریال
    
    کمترین قیمت روز : {arz_price['pond'][2].text} ریال
    
    بیشترین قیمت روز :‌ {arz_price['pond'][3].text} ریال
    
    آخرین ساعت به روز رسانی : {arz_price['pond'][4].text}
    ''')

def frank(update: Updater, context: callbackcontext):

    chat_id = update.message.chat_id
    context.bot.send_chat_action(chat_id, ChatAction.TYPING)
    update.message.reply_text(f'''
    #فرانکـسوئیس\n
    قیمت زنده : {arz_price['frank'][0].text} ریال
    
    کمترین قیمت روز : {arz_price['frank'][2].text} ریال
    
    بیشترین قیمت روز :‌ {arz_price['frank'][3].text} ریال
    
    آخرین ساعت به روز رسانی : {arz_price['frank'][4].text}
    ''')

def derham(update: Updater, context: callbackcontext):

    chat_id = update.message.chat_id
    context.bot.send_chat_action(chat_id, ChatAction.TYPING)
    update.message.reply_text(f'''
    #درهمـامارات\n
    قیمت زنده : {arz_price['derham'][0].text} ریال
    
    کمترین قیمت روز : {arz_price['derham'][2].text} ریال
    
    بیشترین قیمت روز :‌ {arz_price['derham'][3].text} ریال
    
    آخرین ساعت به روز رسانی : {arz_price['derham'][4].text}
    ''')
def lir(update: Updater, context: callbackcontext):

    chat_id = update.message.chat_id
    context.bot.send_chat_action(chat_id, ChatAction.TYPING)
    update.message.reply_text(f'''
    #لیرـترکیه\n
    قیمت زنده : {arz_price['lir'][0].text} ریال
    
    کمترین قیمت روز : {arz_price['lir'][2].text} ریال
    
    بیشترین قیمت روز :‌ {arz_price['lir'][3].text} ریال
    
    آخرین ساعت به روز رسانی : {arz_price['lir'][4].text}
    ''')
def youan(update: Updater, context: callbackcontext):

    chat_id = update.message.chat_id
    context.bot.send_chat_action(chat_id, ChatAction.TYPING)
    update.message.reply_text(f'''
    #یوانـچین\n
    قیمت زنده : {arz_price['youan'][0].text} ریال
    
    کمترین قیمت روز : {arz_price['youan'][2].text} ریال
    
    بیشترین قیمت روز :‌ {arz_price['youan'][3].text} ریال
    
    آخرین ساعت به روز رسانی : {arz_price['youan'][4].text}
    ''')
def yen(update: Updater, context: callbackcontext):

    chat_id = update.message.chat_id
    context.bot.send_chat_action(chat_id, ChatAction.TYPING)
    update.message.reply_text(f'''
    #ینـژاپن\n
    قیمت زنده : {arz_price['yen'][0].text} ریال
    
    کمترین قیمت روز : {arz_price['yen'][2].text} ریال
    
    بیشترین قیمت روز :‌ {arz_price['yen'][3].text} ریال
    
    آخرین ساعت به روز رسانی : {arz_price['yen'][4].text}
    ''')
def dollar_canada(update: Updater, context: callbackcontext):

    chat_id = update.message.chat_id
    context.bot.send_chat_action(chat_id, ChatAction.TYPING)
    update.message.reply_text(f'''
    #دلارـکانادا\n
    قیمت زنده : {arz_price['dollar_canada'][0].text} ریال
    
    کمترین قیمت روز : {arz_price['dollar_canada'][2].text} ریال
    
    بیشترین قیمت روز :‌ {arz_price['dollar_canada'][3].text} ریال
    
    آخرین ساعت به روز رسانی : {arz_price['dollar_canada'][4].text}
    ''')
