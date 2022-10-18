from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import * 


app = ApplicationBuilder().token("5795904473:AAHCz4RlkGOrGKMbZfO76m8k_SndCHe2FYE").build()


app.add_handler(CommandHandler("hello", hello_command))

print('server start')
app.run_polling()