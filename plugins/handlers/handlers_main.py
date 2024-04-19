from pyrogram import filters
from pyromod import Client
from pyrogram.types import Message


@Client.on_message(filters.new_chat_members)
async def welcome(client: Client, m: Message):
    new_members = m.new_chat_members
    text_unformatted = (
        "Hello {name_link} - <code>{user_id}</code>, welcome to <code>"
        + str(m.chat.id)
        + "</code>"
    )
    for user in new_members:
        user_id = user.id
        first_name = user.first_name.replace("<", "").replace(">", "")
        link = f"<a href='tg://user?id={user_id}'>{first_name}</a>"
        text = text_unformatted.format(name_link=link, user_id=user_id)
        await m.reply(text, disable_web_page_preview=True, quote=True)


@Client.on_message(filters.left_chat_member)
async def left(client: Client, m: Message):
    user = m.left_chat_member
    user_id = user.id
    first_name = user.first_name.replace("<", "").replace(">", "")
    link = f"<a href='tg://user?id={user_id}'>{first_name}</a>"
    text = f"go to ass {link} - <code>{user_id}</code>"
    await m.reply(text, disable_web_page_preview=True, quote=True)
