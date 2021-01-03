from telegram.ext import Updater, CommandHandler, callbackcontext
from telegram import Update, ReplyKeyboardMarkup
from telegram.chataction import ChatAction
from telegram.ext import MessageHandler
from telegram.ext.filters import Filters
from currency import *
from coin_gold import *
from crypto import *
from stock import *
from data import date
from decouple import config


token = config("TOKEN")
date = date()

def main_menu_handler(update: Update, context: callbackcontext):
    dollar_emoji = '\U0001F4B5'
    coin_emoji = '\U0001F4B0'
    stock_emoji = '\U0001F4B9'
    crypto_emoji = '\U0001F4C8'
    buttons = [
        [f"{coin_emoji} قیمت طلا و سکه",
        f"{dollar_emoji} نرخ ارز"],
        [f"{crypto_emoji} ارزهای دیجیتال",
        f"{stock_emoji}  بورس"],
        ["تبدیل ارز"]
    ]
    update.message.reply_text(text="منو اصلی",
    reply_markup= ReplyKeyboardMarkup(buttons, resize_keyboard=True))

def start_handler(update: Update, context: callbackcontext):
    chat_id = update.message.chat_id
    first_name = update.message.chat.first_name
    context.bot.send_chat_action(chat_id, ChatAction.TYPING)
    update.message.reply_text(f"سلام {first_name} عزیز.\nبه 'چ‌خبر' خوش اومدی!")
    main_menu_handler(update, context)

def sekke_gold(update: Update, context: callbackcontext):
    buttons = [
        ["طلای ۲۴ عیار","طلای ۱۸ عیار"],
        ["سکه امامی","سکه بهار آزادی"],
        ["ربع سکه", "نیم سکه"],
        ["بازگشت"]
    ]
    update.message.reply_text(text=f"قیمت طلا و سکه در تاریخ {date}",
    reply_markup= ReplyKeyboardMarkup(buttons, resize_keyboard=True))

def exchange(update: Update, context: callbackcontext):
    buttons = [
        ["بازگشت \U0001F519"]
    ]
    text = '''
    برای تبدیل ارز از الگوهای زیر استفاده کنید : 
    
    مثال : ۱۵ دلار به ریال
    
    مثال : ۱۵۰۰۰۰ ریال به دلار
    
    *فعلا تبدیل ارزهای دلار و ریال امکان‌پذیر است.
    *اعداد اعشاری موجب بروز خطای محاسباتی می‌شوند.
    برای مثال : ۳۴.۶ دلار به ریال'''
    update.message.reply_text(text=f"{text}",
    reply_markup= ReplyKeyboardMarkup(buttons, resize_keyboard=True))


def arz(update: Update, context: callbackcontext):
    buttons = [
        ["پوند انگلیس","یورو", "دلار آمریکا"],
        ["لیر ترکیه", "درهم امارات","فرانک سوئیس"],
        ["دلار کانادا", "ین ژاپن","یوان چین"],
        ["بازگشت \U0001F519"]
    ]
    update.message.reply_text(text=f"نرخ ارز در تاریخ {date}",
    reply_markup= ReplyKeyboardMarkup(buttons, resize_keyboard=True))

def crypto(update: Update, context: callbackcontext):
    buttons = [
        ["تتر","اتریوم", "بیت‌کوین"],
        ["دش", "ریپل","لایت‌کوین"],
        ["بازگشت \U0001F519"]
    ]
    update.message.reply_text(text=f"نرخ ارزهای دیجیتال در تاریخ {date}",
    reply_markup= ReplyKeyboardMarkup(buttons, resize_keyboard=True))

def return_handler(update: Updater, context: callbackcontext):
    main_menu_handler(update, context)



def main():
    updater = Updater(token, use_context=True)
    updater.dispatcher.add_handler(CommandHandler("start", start_handler))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex("قیمت طلا و سکه"), sekke_gold))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex("نرخ ارز"), arz))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex("ارزهای دیجیتال"), crypto))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex("تبدیل ارز"), exchange))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex("بازگشت"), return_handler))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex("سکه بهار آزادی"), bahar))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex("سکه امامی"), emami))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex("نیم سکه"), nim))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex("ربع سکه"), rob))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex("طلای ۱۸ عیار"), gold_18))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex("طلای ۲۴ عیار"), gold_24))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex("دلار آمریکا"),dollar_usa))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex("یورو"), euro))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex("پوند انگلیس"), pond))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex("فرانک سوئیس"), frank))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex("درهم امارات"), derham))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex("لیر ترکیه"), lir))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex("یوان چین"), youan))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex("ین ژاپن"), yen))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex("دلار کانادا"), dollar_canada))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex("بورس"), stock_price))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex("بیت‌کوین"), bitcoin))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex("اتریوم"), etherium))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex("تتر"), tether))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex("دش"), dash))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex("ریپل"), riple))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex("لایت‌کوین"), litecoin))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex("\d دلار به ریال"), dollar_to_rial))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex("\d ریال به دلار"), rial_to_dollar))
    updater.start_polling()
    updater.idle()

main()
