from telegram.ext import Updater, CommandHandler
import requests

TOKEN = "7031454507:AAGBjPf4tqz77mPN-mANQffCwBcSwpsPKzU"

def fofa_search(update, context):
    email = "jasetac827@agromgt.com"
    key = "aba76b23c60e66df6879d6d55743f479"
    
    search_query = "your_fofa_search_query_here"
    url = f"https://fofa.so/api/v1/search/all?email={email}&key={key}&qbase64={search_query}"
    
    response = requests.get(url)
    results = response.json()
    
    update.message.reply_text(str(results))

def main():
    updater = Updater(TOKEN)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("fofa_search", fofa_search))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()