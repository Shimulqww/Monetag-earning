from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes import asyncio

LINKS = [ "https://otieu.com/4/9374528", "https://otieu.com/4/9374511", "https://otieu.com/4/9374533", "https://otieu.com/4/9374535" ]

GROUP_LINK = "https://t.me/moneyanouncement"  # Telegram group link

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE): user = update.effective_user keyboard = [[InlineKeyboardButton(f"Visit Link {i+1}", url=link)] for i, link in enumerate(LINKS)] keyboard.append([InlineKeyboardButton("✅ I Have Visited All", callback_data="verify_links")]) await update.message.reply_text( f"Welcome {user.first_name}!\n\nPlease visit all the links below before joining:", reply_markup=InlineKeyboardMarkup(keyboard) )

async def verify(update: Update, context: ContextTypes.DEFAULT_TYPE): query = update.callback_query await query.answer() await query.edit_message_text("Verifying your visit... Please wait 10 seconds.") await asyncio.sleep(10) await query.message.reply_text(f"✅ Verified! Click below to join:\n{GROUP_LINK}")

def main(): from config import TOKEN app = ApplicationBuilder().token(TOKEN).build() app.add_handler(CommandHandler("start", start)) app.add_handler(CallbackQueryHandler(verify, pattern="verify_links")) app.run_polling()

if name == "main": main()
