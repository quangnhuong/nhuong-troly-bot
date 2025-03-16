from telegram.ext import Application, CommandHandler
import os

# Lấy token từ biến môi trường
TOKEN = os.environ.get('TELEGRAM_API_TOKEN')

# Khởi tạo Application
application = Application.builder().token(TOKEN).build()

# Lệnh /start (bất đồng bộ)
async def start(update, context):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Chào mừng đến với bot!")

# Thêm lệnh vào application
application.add_handler(CommandHandler('start', start))

# Khởi động bot
application.run_polling()