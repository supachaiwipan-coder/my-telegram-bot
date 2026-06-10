from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="บอททำงานแล้วครับพี่!")

if __name__ == '__main__':
    # ใส่ Token ของพี่ตรงนี้
    TOKEN = '8845436697:AAETQbeDqlJ9zu2zK4tNGJnuebD8gjMqN8o'
    application = ApplicationBuilder().token(TOKEN).build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    application.run_polling()
