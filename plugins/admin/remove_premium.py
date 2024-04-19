from pyrogram import filters
from pyromod import Client
from pyrogram.types import Message
from utilsdf.db import Database
from utilsdf.vars import PREFIXES
from main import CHANNEL_LOGS


@Client.on_message(filters.command("delp", PREFIXES))
async def delp(client: Client, m: Message):
    user_id = m.from_user.id
    with Database() as db:
        if not db.is_admin(user_id):
            return
        id = m.text[len(m.command[0]) + 2 :].strip()
        if not id or (id[0] != "-" and not id.isdigit()) or not id[1:].isdigit():
            return await m.reply(
                "<b>Ingresa una ID valida para resetear!</b>", quote=True
            )
        func = db.rename_premium
        if id[0] == "-":
            func = db.remove_group
        result = func(id)
        if result is None:
            return await m.reply(
                "<b>La ID no se encuentra en la base de datos!</b>", quote=True
            )
        await m.reply(f"<b>La ID <code>{id}</code> ha sido reseteada!</b>", quote=True)
        await client.send_message(
            CHANNEL_LOGS,
            f"""#premium_deleted

id -» <a href='tg://user?id={id}'>{id}</a>
banned by -»  <a href='tg://user?id={user_id}'>{m.from_user.first_name}</a> [Admin]""",
        )
