import os
from telegram.ext import ApplicationBuilder, CommandHandler

async def start(update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="บอททำงานแล้วครับพี่! ระบบพร้อม!")

if __name__ == '__main__':
    # ตรวจสอบว่าดึง TOKEN มาจาก Render ได้จริง
    TOKEN = os.getenv('TOKEN')
    if not TOKEN:
        print("Error: TOKEN ไม่พบ! กรุณาเช็ค Environment Variables ใน Render")
    else:
        application = ApplicationBuilder().token(TOKEN).build()
        application.add_handler(CommandHandler('start', start))
        application.run_polling()
