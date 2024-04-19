from datetime import datetime
from pyrogram import filters
from pyromod import Client
from pyrogram.types import Message
from utilsdf.vars import PREFIXES
from utilsdf.db import Database
from utilsdf.functions import get_message_from_pyrogram

Fucker_504 = 1115269159


@Client.on_message(filters.command(["plan"], PREFIXES))
async def plan(client: Client, m: Message):
    message = get_message_from_pyrogram(m)
    getting_info = False
    text = m.text[len(m.command[0]) + 2 :].strip()
    if text.isdigit():
        text_id = int(text)
        message = await client.get_users(text_id)
        getting_info = True
    elif text.startswith("@"):
        message = await client.get_users(text)
        getting_info = True
    else:
        user_id = message.from_user.id

    if getting_info:
        first_name = message.first_name
        user_name = message.username
        user_id = message.id
    else:
        first_name = message.from_user.first_name.replace("<", "").replace(">", "")
        user_name = message.from_user.username
    name = f"<a href='tg://user?id={user_id}'>{first_name}</a>"

    with Database() as db:
        info_user = db.get_info_user(user_id)

    membership = info_user["MEMBERSHIP"].capitalize()
    registered = info_user["REGISTERED"]
    registered = datetime.strptime(registered, "%Y-%m-%d %H:%M:%S")
    registered = registered.strftime("%y/%m/%d - %I:%M%p")
    antispam = info_user["ANTISPAM"]
    credits = info_user["CREDITS"]
    rol = info_user["RANK"] if Database.ID_OWNER != user_id else "Owner"
    rol = rol.capitalize()
    if user_id == Fucker_504:
        rol = "Co-Founder"
    rol = f"\n𝙍𝙤𝙡 -» <code>{rol}</code>" if rol.lower() != "user" else ""
    nick = info_user["NICK"]
    expiraton_premium = info_user["EXPIRATION"] if info_user["EXPIRATION"] else ""
    if expiraton_premium:
        now = datetime.strptime(expiraton_premium, "%Y-%m-%d %H:%M:%S")

        diff = now - datetime.now()

        days = diff.days
        total_seconds = diff.seconds
        hours, total_seconds = divmod(total_seconds, 3600)
        minutes, seconds = divmod(total_seconds, 60)

        expiraton_premium = (
            f"\n𝙀𝙭𝙥 -» <code>{days}d-{hours}h-{minutes}m-{seconds}s</code>"
        )
    checks = "2" if membership == "Premium" else "1"
    antispam = str(antispam) + " - " + checks

    text = f"""
- - - - - - - -『𝙐𝙨𝙚𝙧』- - - - - - - -
𝙄𝙙 -» <code>{user_id}</code>
𝙉𝙖𝙢𝙚 -» {name}
𝙐𝙨𝙚𝙧 -» <code>{user_name}</code>
𝙋𝙡𝙖𝙣 -» <code>{membership}</code>
𝙎𝙥𝙖𝙢 -» <code>{antispam}</code> {rol} {expiraton_premium}
𝘾𝙧𝙚𝙙𝙞𝙩𝙨 -» <code>{credits}</code>
𝙉𝙞𝙘𝙠 -» <code>{nick}</code>
𝙍𝙚𝙜 -» <code>{registered}</code>
"""
    await m.reply(text, quote=True, disable_web_page_preview=True)
