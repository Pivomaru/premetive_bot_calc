from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from spy import *

async def hello_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update,context)
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update,context)
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x + y}')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update,context)
    await update.message.reply_text(f'/hello\n/help\n/sum\n/mult\n/div\n/subtraction')


async def div_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update,context)
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} / {y} = {x / y}')

async def subtraction_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update,context)
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} - {y} = {x - y}')

async def mult_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update,context)
    msg = update.message.text
    items = msg.split()
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} * {y} = {x * y}')