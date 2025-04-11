
from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import os

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

app = Client("taker_motivation_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# رسالة البداية
@app.on_message(filters.command("start"))
async def start(client, message):
    welcome = (
        f"مرحباً {message.from_user.first_name}!\n\n"
        "أهلاً بك في بوت التحفيز الخاص بشركة **تيكر**!\n"
        "شارك البوت مع أصدقائك، وكل جهة اتصال تكسبك نقاط وأرباح إضافية!\n\n"
        "ابدأ الآن!"
    )
    
    keyboard = ReplyKeyboardMarkup(
        [
            [KeyboardButton("مشاركة جهة الاتصال", request_contact=True)],
            [KeyboardButton("رؤية فرص الأرباح")],
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )

    await message.reply(welcome, reply_markup=keyboard)

# عند إرسال جهة اتصال
@app.on_message(filters.contact)
async def contact_received(client, message):
    contact_name = message.contact.first_name
    phone_number = message.contact.phone_number
    await message.reply(f"تم استلام جهة الاتصال: {contact_name}\nرقم: {phone_number}\n\nتمت إضافة نقاط إلى حسابك!")

# رؤية فرص الأرباح
@app.on_message(filters.regex("رؤية فرص الأرباح"))
async def show_opportunities(client, message):
    text = (
        "فرصتك للربح من تيكر:\n"
        "- شارك البوت مع أصدقائك\n"
        "- كل جهة اتصال تُضاف = 10 نقاط\n"
        "- تابع تقدمك أسبوعياً\n\n"
        "لمزيد من التفاصيل، تواصل معنا."
    )

    inline = InlineKeyboardMarkup([
        [InlineKeyboardButton("رابط شركة تيكر", url="https://taker.com")],
        [InlineKeyboardButton("اتصل بالدعم", url="https://t.me/YourSupportUsername")]
    ])

    await message.reply(text, reply_markup=inline)

app.run()

