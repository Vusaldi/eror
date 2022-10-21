from pyrogram import Client, filters
from pyrogram.types import Message
from config import BOT_NAME, SUDO
from ERROR.komutlar.start import *
import time

@Client.on_message(
	filters.command(["post", f"post@{BOT_NAME}"])
	& (filters.private | filters.group)
)
async def pstt(client, message):
	reply = message.reply_to_message
	if message.from_user.id in SUDO:
		if not reply:
			await message.reply_text("Lütfen bir mesaja yanıt ver.")
			return
		if reply:
			for i in POST:
				c = await reply.copy(i)
				time.sleep(0.5)
			await message.reply_text("Mesaj iletildi.")
			await client.pin_chat_message(chat_id=i, message_id=c, disable_notification=True)
			return

	else:
		await message.reply_text("Malesef sen SUDO kullanıcı değilsin.")
		return
