from pyrogram import filters
from pyromod import Client
from pyrogram.types import Message
from utilsdf.db import Database
from utilsdf.vars import PREFIXES
from main import CHANNEL_LOGS
from re import findall


@Client.on_message(filters.command("gkey", PREFIXES))
async def gkey(client: Client, m: Message):
    user_id = m.from_user.id
    with Database() as db:
        if not db.is_seller_or_admin(user_id):
            return
        data = findall(r"\d+", m.text)
        days = 1
        if len(data) >= 1:
            days = data[0]
        quantity = 1
        if len(data) >= 2:
            quantity = data[1]
        keys = ""
        for i in range(int(quantity)):
            key = db.gen_key(int(days))
            keys += f"𝙆𝙚𝙮 -» <code>{key[0]}</code>\n"

        info_user = db.get_info_user(user_id)

    await m.reply(
        f"""<b>
𝙂𝙚𝙣𝙚𝙧𝙖𝙩𝙚 𝙆𝙚𝙮 𝙎𝙪𝙘𝙘𝙚𝙨

{keys}
𝙌𝙪𝙖𝙣𝙩𝙞𝙩𝙮 -» <code>{quantity}</code>
𝘿𝙖𝙮𝙨 -» <code>{days}</code>
𝙋𝙡𝙖𝙣 -»  <code>Premium</code>        
</b>""",
        quote=True,
    )
    await client.send_message(
        CHANNEL_LOGS,
        f"""#new_key

{keys}
quantity -»  <code>{quantity}</code>
days -»  <code>{days}</code>
key by -»  <a href='tg://user?id={user_id}'>{m.from_user.first_name}</a> [{info_user["RANK"].capitalize()}]""",
    )
