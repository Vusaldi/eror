from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio


@Client.on_message(
    filters.command("id")
    & (filters.group | filters.private)
)
async def ids(client, message):
    reply=message.reply_to_message
    if reply:
        await message.reply_text(f"**Kullanıcı: [{reply.from_user.first_name}](tg://user?id={reply.from_user.id})\nId: `{reply.from_user.id}`\nMessage id: `{reply.message_id}`\nChatId: `{message.chat.id}`**")
        return
    else:
        await message.reply_text(f"**Kullanıcı: [{message.from_user.first_name}](tg://user?id={message.from_user.id})\nId: `{message.from_user.id}`\nMessage id: `{message.message_id}`\nChatId: `{message.chat.id}`**")
        return
    
@Client.on_message(
    filters.command("stat")
    & filters.group
)
async def stam(client, message):
    stat = message.message_id
    b = await message.reply_text(f"**Total Mesaj: {stat}**")
    await asyncio.sleep(9)
    await b.delete()
    
    
@Client.on_message(filters.command(["purge", "temizle"]))
async def purge(client, message):
    reply = message.reply_to_message
    msgids = []
    if not reply:
        await message.reply_text("**Lütfen bir mesaja yanıt ver!!**")
        return
    if reply:
        msj = reply.message_id
        mid = message.message_id
        rng = mid - msj
        for i in range(rng):
            msgids.append(msj)
            msj += 1
        for msg in msgids:
            await client.delete_messages(message.chat.id, msgids)
        await client.delete_messages(message.chat.id, mid)
        cry = len(msgids) + 1
        b = await message.reply_text(f"**İşlem bitti!!\n`{cry}` tane mesaj silindi...**")
        await asyncio.sleep(3)
        await b.delete()
