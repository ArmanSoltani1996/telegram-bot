from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# --- 1. Define your bot token ---
TOKEN = "8329629571:AAF1ZEdbNbifFTlpqjg4nI_IRw_FEBU7_fc"

# --- 2. Define your command functions ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Hello! I’m your bot and I’m running locally.")

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🧠 Available commands:\n/start - start bot\n/help - show this message")

# --- 3. Setup the bot application ---
app = Application.builder().token(TOKEN).build()

# --- 4. Add command handlers ---
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help))

# --- 5. Run the bot ---
print("✅ Bot is running... Press Ctrl + C to stop.")
app.run_polling()