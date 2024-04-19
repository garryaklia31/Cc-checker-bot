from pyrogram import filters
from pyromod import Client
from pyrogram.types import Message
from pyrogram.enums import ChatType
from utilsdf.vars import PREFIXES
from utilsdf.functions import get_message_from_pyrogram


@Client.on_message(
    filters.command(["id", "perfil", "about", "profile", "me", "my", "info"], PREFIXES)
)
async def id_chat(client: Client, m: Message):
    message = get_message_from_pyrogram(m)
    user_id = message.from_user.id
    first_name = message.from_user.first_name.replace("<", "").replace(">", "")
    name = f"<a href='tg://user?id={user_id}'>{first_name}</a>"
    user_name = message.from_user.username
    chat_type = m.chat.type
    text = f"""
- - - - - - - -『𝙐𝙨𝙚𝙧』- - - - - - - -
𝙄𝙙 -» <code>{user_id}</code>
𝙉𝙖𝙢𝙚 -» {name}
𝙐𝙨𝙚𝙧 -» <code>{user_name}</code>
"""
    if chat_type != ChatType.PRIVATE:
        chat_id = m.chat.id
        chat_name = m.chat.title
        text += f"""- - - - - - - -『𝙂𝙧𝙤𝙪𝙥』- - - - - - - -
𝙄𝙙 -» <code>{chat_id}</code>
𝙉𝙖𝙢𝙚 -» <code>{chat_name}</code>
𝙏𝙮𝙥𝙚 -» <code>{str(chat_type).replace("ChatType.", "").lower()}</code>
"""
    await m.reply(text, quote=True, disable_web_page_preview=True)
