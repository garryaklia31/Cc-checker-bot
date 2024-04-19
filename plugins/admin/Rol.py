from pyrogram import filters
from pyromod import Client
from pyrogram.types import Message
from utilsdf.db import Database
from re import findall
from utilsdf.vars import PREFIXES
from main import CHANNEL_LOGS

FORMAT_CMD = "<b>Formato: <code>/set_rol seller|admin USER_ID</code></b>"


@Client.on_message(filters.command("set_rol", PREFIXES))
async def rol(client: Client, m: Message):
    user_id = m.from_user.id
    with Database() as db:
        if not db.is_admin(user_id):
            return
        data = str(m.text[len(m.command[0]) + 2 :].strip())
        data_split = data.split(" ")

        if len(data_split) <= 1 or data_split[0].lower() not in ["seller", "admin"]:
            return await m.reply(FORMAT_CMD)
        rank = data_split[0].lower()
        data = findall(r"\d+", data)
        if len(data) != 1:
            return await m.reply(FORMAT_CMD, quote=True)
        id = data[0]
        result = None
        if rank == "seller":
            result = db.promote_to_seller(id)
        elif rank == "admin":
            result = db.promote_to_admin(id)

        if result is None:
            return await m.reply(
                "<b>La ID no se encuentra en la base de datos!\nPidele al usuario que hable con el bot!</b>",
                quote=True,
            )
        await m.reply(
            f"""<b>
La ID <code>{id}</code> ha sido promovida a {rank}
</b>""",
            quote=True,
        )
        await client.send_message(
            CHANNEL_LOGS,
            f"""#new_user_rol

id -» <a href='tg://user?id={id}'>{id}</a>
rol -»  <code>{rank.capitalize()}</code>
rol by -»  <a href='tg://user?id={user_id}'>{m.from_user.first_name}</a>""",
        )
