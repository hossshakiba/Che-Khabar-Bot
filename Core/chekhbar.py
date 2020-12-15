from telegram.ext import Updater, CommandHandler, callbackcontext
from telegram import Update, ReplyKeyboardMarkup
from telegram.chataction import ChatAction
from telegram.ext import MessageHandler
from telegram.ext.filters import Filters
from currency import *
from coin import *
from crypto import *
from stock import *
from data import date

token = "1480823735:AAEanwEgggt8VWm3VH8MvVcU-WNuFHSRgac"
date = date()

def main_menu_handler(update: Update, context: callbackcontext):
    buttons = [
        ["قیمت سکه","نرخ ارز"],
        ["ارزهای دیجیتال", "بورس"],
        ["راهنمای خرید"]
    ]
    update.message.reply_text(text="منو اصلی",
    reply_markup= ReplyKeyboardMarkup(buttons, resize_keyboard=True))

def start_handler(update: Update, context: callbackcontext):
    chat_id = update.message.chat_id
    first_name = update.message.chat.first_name
    context.bot.send_chat_action(chat_id, ChatAction.TYPING)
    update.message.reply_text(f"سلام {first_name} عزیز.\nبه 'چ‌خبر' خوش اومدی!")
    main_menu_handler(update, context)

def sekke(update: Update, context: callbackcontext):
    buttons = [
        ["سکه امامی","سکه بهار آزادی"],
        ["ربع سکه", "نیم سکه"],
        ["بازگشت"]
    ]
    update.message.reply_text(text=f"قیمت سکه در تاریخ {date}",
    reply_markup= ReplyKeyboardMarkup(buttons, resize_keyboard=True))


def arz(update: Update, context: callbackcontext):
    buttons = [
        ["پوند انگلیس","یورو", "دلار آمریکا"],
        ["لیر ترکیه", "درهم امارات","فرانک سوئیس"],
        ["دلار کانادا", "ین ژاپن","یوان چین"],
        ["بازگشت"]
    ]
    update.message.reply_text(text=f"نرخ ارز در تاریخ {date}",
    reply_markup= ReplyKeyboardMarkup(buttons, resize_keyboard=True))

def crypto(update: Update, context: callbackcontext):
    buttons = [
        ["تتر","اتریوم", "بیت‌کوین"],
        ["دش", "ریپل","لایت‌کوین"],
        ["بازگشت"]
    ]
    update.message.reply_text(text=f"نرخ ارزهای دیجیتال در تاریخ {date}",
    reply_markup= ReplyKeyboardMarkup(buttons, resize_keyboard=True))


def about(update: Updater, context: callbackcontext):
    chat_id = update.message.chat_id
    context.bot.send_chat_action(chat_id, ChatAction.TYPING)
    
    update.message.reply_text(f'فعلا هیچی....')
def return_handler(update: Updater, context: callbackcontext):
    main_menu_handler(update, context)



def main():
    updater = Updater(token, use_context=True)
    updater.dispatcher.add_handler(CommandHandler("start", start_handler))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex("قیمت سکه"), sekke))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex("نرخ ارز"), arz))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex("ارزهای دیجیتال"), crypto))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex("بازگشت"), return_handler))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex("درباره ما"), about))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex("سکه بهار آزادی"), bahar))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex("سکه امامی"), emami))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex("نیم سکه"), nim))
    updater.dispatcher.add_handler(MessageHandler(Filters.regex("ربع سکه"), rob))
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
    updater.start_polling()
    updater.idle()

main()
