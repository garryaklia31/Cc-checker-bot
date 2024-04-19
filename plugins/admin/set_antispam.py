from pyrogram import filters
from pyromod import Client
from pyrogram.types import Message
from utilsdf.db import Database
from re import findall
from utilsdf.vars import PREFIXES


FORMAT_CMD = "<b>Formato: <code>/antispam USER_ID ANTISPAM</code></b>"


@Client.on_message(filters.command("antispam", PREFIXES))
async def spam(client: Client, m: Message):
    user_id = m.from_user.id
    with Database() as db:
        if not db.is_admin(user_id):
            return
        text = m.text[len(m.command[0]) + 2 :].strip()
        data_nums = findall(r"\d+", text)
        if len(data_nums) != 2:
            return await m.reply(FORMAT_CMD, quote=True)
        id = data_nums[0]
        antispam = data_nums[1]
        result = db.set_antispam(id, antispam)
        if result is None:
            return await m.reply(
                "<b>La ID no se encuentra en la base de datos!\nPidele al usuario que hable con el bot!</b>",
                quote=True,
            )
        await m.reply(
            f"""<b>
La ID <code>{id}</code> ahora tiene <code>{antispam}</code> antispam
</b>""",
            quote=True,
        )
