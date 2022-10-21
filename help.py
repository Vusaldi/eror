from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from config import BOT_NAME

@Client.on_message(
	filters.command(["help", f"help@{BOT_NAME}"])
	& (filters.private | filters.group)
)
async def ghelp(client, message):
	await message.reply_text(
f"""
<b>Komutu çalıştıran: {message.from_user.mention}

/ban - Mesajını yanıtladığınız kullanıcıyı banlar.
/kick - Mesajını yanıtladığınız kullanıcıyı grubtan atar.
/ilet - Adminlere istek/öneri iletir.
/sabit - Yanıtladığınız mesajı sabitler.</b>
"""
)
