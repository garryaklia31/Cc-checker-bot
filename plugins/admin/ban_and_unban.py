from pyrogram import filters
from pyromod import Client
from pyrogram.types import Message
from utilsdf.db import Database
from utilsdf.vars import PREFIXES
from main import CHANNEL_LOGS


@Client.on_message(filters.command(["ban", "unban"], PREFIXES))
async def ban_unban(client: Client, m: Message):
    user_id = m.from_user.id
    with Database() as db:
        if not db.is_admin(user_id):
            return
        if len(m.command) != 2 or not m.command[1].isdigit():
            return await m.reply("<b>Ingresa una ID valida!</b>", quote=True)
        command, id = m.command
        ban_user = True if command == "ban" else False
        type_log = "user_banned" if command == "ban" else "user_unbanned"
        text = (
            "<b>La ID <code>{}</code> ha sido baneada exitosamente!</b>"
            if ban_user
            else "<b>La ID <code>{}</code> ha sido desbaneada exitosamente!</b>"
        )
        result = db.unban_or_ban_user(id, ban_user)
        if result is None:
            return await m.reply(
                "<b>La ID <code>{}</code> no se encuentra en mi base de !</b>".format(
                    id
                ),
                quote=True,
            )
        await m.reply(text.format(id), quote=True)
        await client.send_message(
            CHANNEL_LOGS,
            f"""#{type_log}

id -» <a href='tg://user?id={id}'>{id}</a>
banned by -»  <a href='tg://user?id={user_id}'>{m.from_user.first_name}</a> [Admin]""",
        )
