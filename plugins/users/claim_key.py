from pyrogram import filters
from pyromod import Client
from pyrogram.types import Message
from utilsdf.db import Database
from utilsdf.vars import PREFIXES
from main import CHANNEL_LOGS


@Client.on_message(filters.command("claim", PREFIXES))
async def claim(client: Client, m: Message):
    key = m.text[len(m.command[0]) + 2 :].strip()
    if not key or not key.startswith("key-aktz"):
        return await m.reply("<b>Ingresa una key valida!</b>", quote=True)
    user_id = m.from_user.id
    with Database() as db:
        if db.is_seller(user_id):
            return await m.reply(
                "<b>Los sellers no pueden reclamar keys, contacta a @Sachioyt666 o @Fucker_504!</b>",
                quote=True,
            )
        result = db.claim_key(key, user_id)
    if result is None:
        return await m.reply(
            "<b>La key <code>{}</code> no se encuentra en mi base de datos!</b>".format(
                key
            ),
            quote=True,
        )
    await m.reply(
        f"""<b>
La key <code>{key}</code> ha sido reclamada exitosamente!
Expiracion: <code>{result}</code>

</b>""",
        quote=True,
    )
    await client.send_message(
        CHANNEL_LOGS,
        f"""#key_canjed
id -» <code>{user_id}</code>
key -»  <code>{key}</code>
expiration -» <code>{result}</code>
canjed by -»  <a href='tg://user?id={m.from_user.id}'>{m.from_user.first_name}</a>""",
    )
    link = await client.create_chat_invite_link(-1001960831832, member_limit=1)
    await client.unban_chat_member(-1001960831832, user_id)
    await client.send_message(user_id, f"<b>Grupo de usuarios: {link.invite_link}</b>")
