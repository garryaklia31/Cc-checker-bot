from pyrogram import filters
from pyromod import Client
from pyrogram.types import Message
from utilsdf.db import Database
from re import findall
from utilsdf.vars import PREFIXES

FORMAT_CMD = "<b>Formato: <code>/nick USER_ID NICK</code></b>"


@Client.on_message(filters.command("nick", PREFIXES))
async def nick(client: Client, m: Message):
    user_id = m.from_user.id
    with Database() as db:
        if not db.is_admin(user_id):
            return
        text = m.text[len(m.command[0]) + 2 :].strip()
        data_split = text.split(" ")
        if len(data_split) < 2:
            return await m.reply(FORMAT_CMD, quote=True)
        id = data_split[0]
        nick = " ".join(data_split[1:])
        if not id.isdigit():
            return await m.reply(FORMAT_CMD, quote=True)
        result = db.set_nick(id, nick)
        if result is None:
            return await m.reply(
                "<b>La ID no se encuentra en la base de datos!\nPidele al usuario que hable con el bot!</b>",
                quote=True,
            )
        await m.reply(
            f"""<b>
La ID <code>{id}</code> tiene el nick: <code>{nick}</code>
</b>""",
            quote=True,
        )
