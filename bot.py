
import logging
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# إعدادات السجل
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# رسالة البداية
WELCOME_MSG = (
    "مرحباً بك في *شركة التيكر*!

"
    "نحن نقدم لك فرصة مميزة لزيادة أرباحك من خلال الانضمام إلى برنامج الإحالة الخاص بنا.

"
    "هل ترغب بمشاركة رقم هاتفك معنا للاستفادة؟"
)

# لوحة المفاتيح لمشاركة رقم الهاتف
def get_phone_keyboard():
    keyboard = [
        [KeyboardButton("مشاركة رقمي", request_contact=True)]
    ]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True)

# دالة /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(WELCOME_MSG, reply_markup=get_phone_keyboard(), parse_mode="Markdown")

# استقبال رقم الهاتف
async def contact_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    contact = update.effective_message.contact
    phone_number = contact.phone_number
    user = update.effective_user

    # الرد مع رابط الإحالة
    await update.message.reply_text(
        f"شكراً لك {user.first_name}!
"
        f"تم استلام رقمك: {phone_number}

"
        f"للانضمام إلى برنامج الإحالة، استخدم الرابط التالي:
"
        f"https://aitlkerapp.com/#/register/3669662"
    )

# تشغيل البوت
def main():
    TOKEN = os.environ.get("BOT_TOKEN")
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.CONTACT, contact_handler))

    app.run_polling()

if __name__ == "__main__":
    main()
