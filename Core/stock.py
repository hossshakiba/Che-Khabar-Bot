from telegram.ext import Updater, callbackcontext
from telegram.chataction import ChatAction
from data import stock

stock = stock()

def stock_price(update: Updater, context: callbackcontext):

    chat_id = update.message.chat_id
    context.bot.send_chat_action(chat_id, ChatAction.TYPING)
    update.message.reply_text(f'''
    #بورس\n
    شاخص بورس : {stock['shakhes_kol']}
    
    شاخص کل هم‌وزن : {stock['shakhes_kol_hamvazn']}
    
    شاخص کل فرابورس :‌ {stock['shakhes_kol_faraburs']}
    
    ''')