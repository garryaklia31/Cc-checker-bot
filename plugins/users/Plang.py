from pyrogram import filters
from pyromod import Client
from pyrogram.types import Message
from utilsdf.db import Database
from utilsdf.vars import PREFIXES


@Client.on_message(filters.command(["plang"], PREFIXES))
async def id_chat(client: Client, m: Message):
    chat_id = m.chat.id
    chat_name = m.chat.title
    chat_type = m.chat.type
    with Database() as db:
        chat_info = db.get_info_group(chat_id)
    authorized = "Authorized" if chat_info else "No Authorized"
    expiration = f"\n𝙀𝙭𝙥 -» <code>{chat_info['EXPIRATION']}</code>" if chat_info else ""
    text = f"""
𝙄𝙙 -» <code>{chat_id}</code>
𝙉𝙖𝙢𝙚 -» <code>{chat_name}</code>
𝙏𝙮𝙥𝙚 -» <code>{str(chat_type).replace("ChatType.", "").lower()}</code>
𝙋𝙡𝙖𝙣 -» <code>{authorized}</code> {expiration}
"""
    await m.reply(text, quote=True, disable_web_page_preview=True)
