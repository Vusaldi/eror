from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, ChatPermissions
from config import BOT_NAME, SUDO
from pyrogram.errors import UserAdminInvalid

BAN_YT = []

@Client.on_message(
	filters.command("ytban")
	& filters.group
)
async def ytban(client, message):
	reply = message.reply_to_message

	if message.from_user.id in SUDO:

		if not reply:
			await message.reply_text("Malesef bir kullanıcıya yanıt vermedin.")
			return

		if reply:
			user = reply.from_user.id
			if user in BAN_YT:
				await message.reply_text("Malesef bu kullanıcı zaten botta **BAN** yetkisine sahip.")
			else:
				BAN_YT.append(user)
				await message.reply_text("Kullanıcı `BAN_YT` listesine eklendi.")
	else:
		await message.reply_text("Malesef sen **SUDO** kullanıcı değilsin.")
		return

@Client.on_message(
	filters.command("rmban")
	& filters.group
)
async def rmban(client, message):
	rep = message.reply_to_message

	if message.from_user.id in SUDO:

		if not rep:
			await message.reply_text("Malesef bir kullanıcıya yanıt vermedin.")
			return

		if rep:
			us = rep.from_user.id
			if us in BAN_YT:
				BAN_YT.remove(rep.from_user.id)
				await message.reply_text("Kullanıcı `BAN_YT` listesine çıkartıldı.")
			else:
				await message.reply_text("<b>Malesef zaten listede olmayan bir kullanıcıyı nasıl listeden çıkartmamı bekliyorsun?</b>")

	else:
		await message.reply_text("Malesef sen SUDO kullanıcı değilsin.")
		return


@Client.on_message(
	filters.command(["ban", f"ban@{BOT_NAME}"])
	& filters.group
)
async def ban(client, message):
	repl = message.reply_to_message
	async for member in client.iter_chat_members(message.chat.id, filter="administrators"):
		if message.from_user.id in BAN_YT:
			try:
				if not repl:
					await message.reply_text("Malesef bir kullanıcıya yanıt vermedin.")
					return
				else:
					await client.kick_chat_member(message.chat.id, repl.from_user.id)

					await message.reply_text(f"{repl.from_user.mention} banlandı.\n\nYetkili: {message.from_user.mention}")
					return
			except UserAdminInvalid:
				await message.reply_text("Bir yöneticiyi grubtan atmamı nasıl düşünürsün 🙄")
				return
			
		if not message.from_user.id in BAN_YT:
			await message.reply_text("Malesef BAN yetkisine sahip değilsin :(")
			return

@Client.on_message(
	filters.command(["unban", f"unban@{BOT_NAME}"])
	& filters.group
)
async def unban(client, message):
	async for member in client.iter_chat_members(message.chat.id, filter="administrators"):
		if message.from_user.id in BAN_YT:
			repl = message.reply_to_message

			if not repl:
				await message.reply_text("Malesef bir kullanıcıya yanıt vermedin.")
				return
			else:

				await client.unban_chat_member(message.chat.id, repl.from_user.id)
				await message.reply_text(f"{repl.from_user.mention} banı kaldırıldı.")
				return
		if not message.from_user.id in BAN_YT:
			await message.reply_text("Malesef BAN yetkisine sahip değilsin :(")
			return
