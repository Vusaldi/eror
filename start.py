from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from config import BOT_NAME
from ERROR.komutlar.stats import *

POST = [] 

@Client.on_message(
	filters.command(["start", f"start@{BOT_NAME}"])
	& (filters.private | filters.group)
)
async def start(client, message):
	if message.chat.type == "private":
		if not message.chat.id in PRV:
			PRV.append(message.chat.id)
			POST.append(message.chat.id)
	if message.chat.type == "group":
		if not message.chat.id in GRP:
			GRP.append(message.chat.id)
			POST.append(message.chat.id)
			
	if message.chat.type == "supergroup":
		if not message.chat.id in GRP:
			GRP.append(message.chat.id)
			POST.append(message.chat.id)
			
	await message.reply_text(f"<b>Selam {message.from_user.mention}\n\nBen [ΞЯ404](https://t.me/ER4O4Chat) için yapılan bir botum.\nYardım için: /help\n\nDeveloper: [ReWoxi](https://t.me/ReWoxi)</b>",
		disable_web_page_preview=True,
		reply_markup=InlineKeyboardMarkup(
			[
				[
					InlineKeyboardButton("ΞЯ404", url="https://t.me/ER4O4")
				],
				[
					InlineKeyboardButton("Sohbet", url="https://t.me/ER4O4Chat"),
					InlineKeyboardButton("Developer", url="https://t.me/ReWoxi")
				]
			]
		)
	)
