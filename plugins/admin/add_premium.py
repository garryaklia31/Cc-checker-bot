from pyrogram import filters
from pyromod import Client
from pyrogram.types import Message
from utilsdf.db import Database
from re import findall
from utilsdf.vars import PREFIXES
from main import CHANNEL_LOGS


@Client.on_message(filters.command("addp", PREFIXES))
async def addp(client: Client, m: Message):
    user_id = m.from_user.id
    with Database() as db:
        if not db.is_admin(user_id):
            return
        data = m.text[len(m.command[0]) + 2 :].strip()
        data = findall(r"\d+", data)

        if len(data) != 3:
            return await m.reply("<b>Formato: ID DIAS CREDITOS</b>", quote=True)

        id = data[0]
        days = data[1]

        credits = data[2]
        result = db.add_premium_membership(id, days, credits)
        info_user = db.get_info_user(user_id)
        if result is None:
            return await m.reply(
                "<b>La ID no se encuentra en la base de datos!\nPidele al usuario que ejecute <code>/start</code></b>",
                quote=True,
            )
        await m.reply(
            f"""<b>
La ID <code>{id}</code> ha sido promovida al plan Premium!
Dias: <code>{days}</code>
Creditos: <code>{credits}</code>
Expiracion: <code>{result}</code>
</b>""",
            quote=True,
        )
        await client.send_message(
            CHANNEL_LOGS,
            f"""#new_user_premium_add

id -» <a href='tg://user?id={id}'>{id}</a>
days -» <code>{days}</code>
credits -» <code>{credits}</code>
added by -»  <a href='tg://user?id={user_id}'>{m.from_user.first_name}</a> [{info_user["RANK"].capitalize()}]""",
        )
        link = await client.create_chat_invite_link(-1001494650944, member_limit=1)
        await client.unban_chat_member(-1001494650944, int(id))
        await client.send_message(
            int(id), f"<b>Grupo de usuarios: {link.invite_link}</b>"
        )
