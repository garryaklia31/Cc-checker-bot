import re
from pyrogram import filters
from pyromod import Client
from pyrogram.types import Message
from utilsdf.db import Database
from utilsdf.vars import PREFIXES
from main import CHANNEL_LOGS


@Client.on_message(filters.command("addg", PREFIXES))
async def addg(client: Client, m: Message):
    user_id = m.from_user.id
    with Database() as db:
        if not db.is_seller_or_admin(user_id):
            return await m.reply(
                "<b>You don't have permission to execute this command.</b>", quote=True
            )
        match = re.search(r"(-?\d+)\s+(\d+)", m.text)
        if not match:
            return await m.reply("<b>Format: CHAT_ID DAYS</b>", quote=True)
        chat_id, days = map(int, match.groups())
        if chat_id >= 0:
            return await m.reply("<b>Invalid CHAT_ID!</b>", quote=True)
        result = db.add_group(chat_id, days, m.from_user.username)
        await m.reply(
            f"<b>{days} days have been added to chat {chat_id}!\nExpiration: {result}</b>",
            quote=True,
        )
        await client.send_message(
            CHANNEL_LOGS,
            f"""#new_chat_premium

chat_id -» <a href='tg://user?id={chat_id}'>{chat_id}</a> 
days -»  <code>{days}</code>
added by -»  <a href='tg://user?id={user_id}'>{m.from_user.first_name}</a>""",
        )
