from pyrogram import filters
from pyromod import Client
from pyrogram.types import Message
from utilsdf.db import Database
from utilsdf.functions import (
    anti_bots_telegram,
    get_bin_info,
    get_cc,
    antispam,
    get_text_from_pyrogram,
)
from utilsdf.vars import PREFIXES
from gates.ko import ko
from time import perf_counter


@Client.on_message(filters.command("ko", PREFIXES))
async def ko_cmd(client: Client, m: Message):
    user_id = m.from_user.id
    with Database() as db:
        if not db.is_authorized(user_id, m.chat.id):
            return await m.reply(
                "𝑻𝒉𝒊𝒔 𝒄𝒉𝒂𝒕 𝒊𝒔 𝒏𝒐𝒕 𝒂𝒑𝒑𝒓𝒐𝒗𝒆𝒅 𝒕𝒐 𝒖𝒔𝒆 𝒕𝒉𝒊𝒔 𝒃𝒐𝒕.", quote=True
            )
        user_info = db.get_info_user(user_id)
        is_free_user = user_info["MEMBERSHIP"]
        is_free_user = is_free_user.lower() == "free user"
        if is_free_user:
            captcha = await anti_bots_telegram(m, client)
            if not captcha:
                return
    text = get_text_from_pyrogram(m)
    ccs = get_cc(text)
    if not ccs:
        return await m.reply(
            "𝙂𝙖𝙩𝙚𝙬𝙖𝙮 <code>𝙆𝙤𝙣𝙖𝙣 ♻️ -» $0</code>\n𝙁𝙤𝙧𝙢𝙖𝙩 -» <code>/ko cc|month|year|cvc</code>",
            quote=True,
        )
    ini = perf_counter()
    cc = ccs[0]
    mes = ccs[1]
    ano = ccs[2]
    cvv = ccs[3]


    # check antispam
    antispam_result = antispam(user_id, user_info["ANTISPAM"], is_free_user)
    if antispam_result != False:
        return await m.reply(
            f"𝙋𝙡𝙚𝙖𝙨𝙚 𝙒𝙖𝙞𝙩... -» <code>{antispam_result}'s</code>", quote=True
        )
    msg_to_edit = await m.reply("𝙋𝙡𝙚𝙖𝙨𝙚 𝙒𝙖𝙞𝙩...", quote=True)
    cc_formatted = f"{cc}|{mes}|{ano}|{cvv}"
    result = await ko(cc, mes, ano, cvv)
    if not isinstance(result, tuple):
        status = "Dead! ❌"
        status1 = result
    else:
        st, code, msg, cvc, d_code = result

        if "succeeded" in st:
            status = "Approved! ✅"
            status1 = "Approved"
        elif "pass" in cvc:
            status = "Approved! ✅ -» cvv"
            status1 = "cvc: M"
        elif "insufficient_funds" in code or "Your card has insufficient funds." in msg:
            status = "Approved! ✅ -» low funds"
            status1 = "Insufficient Funds"
        elif "incorrect_cvc" in code:
            status = "Approved! ✅ -» ccn"
            status1 = msg
        elif "card_declined" in code:
            status = "Dead! ❌"
            status1 = msg
        elif "requires_action" in st:
            status = "Dead! ❌"
            status1 = "3D xD"
        else:
            status = "Dead! ❌"
            status1 = d_code if d_code else msg
    final = perf_counter() - ini
    with Database() as db:
        db.increase_checks(user_id)
    text_ = f"""<b>ア 𝘾𝘾 -» <code>{cc_formatted}</code>
カ 𝙎𝙩𝙖𝙩𝙪𝙨 -» <code>{status}</code>
ツ 𝙍𝙚𝙨𝙪𝙡𝙩 -» <code>{status1}</code>

キ 𝘽𝙞𝙣 -» <code></code> - <code></code> - <code></code>
朱 𝘽𝙖𝙣𝙠 -» <code></code>
零 𝘾𝙤𝙪𝙣𝙩𝙧𝙮 -» <code></code> 

⸙ 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 -» <code>𝙆𝙤𝙣𝙖𝙣 -» $0</code>
꫟ 𝙏𝙞𝙢𝙚 -» <code>{final:0.3}'s</code>
ᥫ᭡ 𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮 -» <a href='tg://user?id={m.from_user.id}'>{m.from_user.first_name}</a> []</b>"""

    await msg_to_edit.edit(text_)
