import re

from pyrogram import Client, filters
from pyrogram.types import Message
from utilsdf.db import Database
from utilsdf.functions import get_extras, get_bin_info, get_text_from_pyrogram
from utilsdf.vars import PREFIXES

extras_cache = {}


@Client.on_message(filters.command("extra", PREFIXES))
async def extras(client: Client, m: Message):
    user_id = m.from_user.id
    with Database() as db:
        if not db.is_authorized(user_id, m.chat.id):
            return await m.reply(
                "𝑻𝒉𝒊𝒔 𝒄𝒉𝒂𝒕 𝒊𝒔 𝒏𝒐𝒕 𝒂𝒑𝒑𝒓𝒐𝒗𝒆𝒅 𝒕𝒐 𝒖𝒔𝒆 𝒕𝒉𝒊𝒔 𝒃𝒐𝒕.", quote=True
            )
        # user_info = db.GetInfoUser(user_id)
    text = get_text_from_pyrogram(m)
    if not text:
        return await m.reply("♻️𝙁𝙤𝙧𝙢𝙖𝙩 -» <code>/extra 401658</code>", quote=True)
    extra = re.search(r"[3-7]\d{5,15}", text)
    if not extra:
        return await m.reply("<b>Invalid extra ⚠️</b>", quote=True)
    extra = extra.group()[0:6]
    if extra in extras_cache:
        resp = extras_cache[extra]
    else:
        resp = await get_extras(extra)
        extras_cache[extra] = resp
    if resp is None:
        return await m.reply(
            "<b>No se encontraron resultados para el bin!</b>", quote=True
        )
    extras = "- - - - - - - - - 𝙀𝙭𝙩𝙧𝙖𝙨』- - - - - - - -\n"
    for cc in resp:
        data = re.findall(r"[0-9]+", cc)
        cc = data[0][:-4] + "x" * 4
        month = data[1]
        year = data[2]
        if len(year) == 2:
            year = "20" + year
        formatted_extra = f"<code>{cc}|{month}|{year}</code>"
        extras += formatted_extra + "\n"
    bin_info = await get_bin_info(extra)
    brand = bin_info["brand"]
    country_name = bin_info["country_name"]
    country_flag = bin_info["country_flag"]
    bank = bin_info["bank"]
    level = bin_info["level"]
    typea = bin_info["type"]
    extras += f"""- - - - - - - - - - - - - - - - - - - - -
𝙄𝙣𝙛𝙤 -» <code>{brand}</code> - <code>{typea}</code> - <code>{level}</code>
𝘽𝙖𝙣𝙠 -» <code>{bank}</code>
𝘾𝙤𝙪𝙣𝙩𝙧𝙮 -» <code>{country_name}</code> {country_flag}"""
    await m.reply(extras, quote=True)
