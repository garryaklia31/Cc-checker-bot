import re
from pyrogram import filters
from pyromod import Client
from pyrogram.types import Message
from utilsdf.db import Database
from utilsdf.functions import get_bin_info, get_text_from_pyrogram
from utilsdf.vars import PREFIXES


@Client.on_message(filters.command("bin", PREFIXES))
async def bin_f(client: Client, m: Message):
    user_id = m.from_user.id
    with Database() as db:
        if not db.is_authorized(user_id, m.chat.id):
            return await m.reply(
                "𝑻𝒉𝒊𝒔 𝒄𝒉𝒂𝒕 𝒊𝒔 𝒏𝒐𝒕 𝒂𝒑𝒑𝒓𝒐𝒗𝒆𝒅 𝒕𝒐 𝒖𝒔𝒆 𝒕𝒉𝒊𝒔 𝒃𝒐𝒕.", quote=True
            )
        user_info = db.get_info_user(user_id)
    text = get_text_from_pyrogram(m)
    if not text:
        return await m.reply("𝘽𝙞𝙣\n♻️𝙁𝙤𝙧𝙢𝙖𝙩 -» <code>/bin 666666</code>", quote=True)

    bin_i = re.search(r"[3-7]\d{5,15}", text)

    if not bin_i:
        return await m.reply("𝙄𝙣𝙫𝙖𝙡𝙞𝙙 𝘽𝙞𝙣 ⚠️", quote=True)
    bin_i = bin_i.group()[0:6]
    resp = await get_bin_info(bin_i)
    if resp is None:
        return await m.reply(
            "<b>No se encontraron resultados para el bin!</b>", quote=True
        )
    bin_i = resp["bin"]
    brand = resp["brand"]
    country_name = resp["country_name"]
    country_flag = resp["country_flag"]
    bank = resp["bank"]
    level = resp["level"] if resp["level"] else "UNAVAILABLE"
    typea = resp["type"] if resp["type"] else "UNAVAILABLE"
    rol = user_info["RANK"].capitalize()
    nick = user_info["NICK"]
    await m.reply(
        f"""<b>𝘽𝙞𝙣 -» <code>{bin_i}</code>
- - - - - - - - - - - - - - - - - - - - -
𝙄𝙣𝙛𝙤 -» <code>{brand}</code> - <code>{typea}</code> - <code>{level}</code>
𝘽𝙖𝙣𝙠 -» <code>{bank}</code>
𝘾𝙤𝙪𝙣𝙩𝙧𝙮 -» <code>{country_name}</code> {country_flag}
- - - - - - - - - - - - - - - - - - - - -
𝘾𝙝𝙚𝙘𝙠𝙚𝙙 <a href='tg://user?id={m.from_user.id}'>{m.from_user.first_name}</a> [{rol}] -» <code>{nick}</code>

    </b>""",
        quote=True,
    )
