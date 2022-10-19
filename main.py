from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import * 


app = ApplicationBuilder().token("579\****************************CHe2FYE").build()


app.add_handler(CommandHandler("hello", hello_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("subtraction", subtraction_command))
app.add_handler(CommandHandler("mult", mult_command))
app.add_handler(CommandHandler("div", div_command))


print('server start')
app.run_polling()
