from pyrogram import filters
from pyromod import Client
from pyrogram.types import Message
from utilsdf.db import Database
from utilsdf.functions import (
    get_bin_info,
    get_cc,
    antispam,
    get_text_from_pyrogram,
    get_gate_by_cmd,
    handler_gate,
)

from json import load
from utilsdf.vars import PREFIXES
from time import perf_counter
from utilsdf.gates_for_mass import (
    boruto,
    darkito,
    lynx,
    rohee,
    stripe_gate,
    ass,
    ka,
    ko,
    astharoth,
    autoshopify,
)

with open("assets/gates.json", "r", encoding="utf-8-sig") as json_file:
    gates_data = load(json_file)

cmds = set(gate["cmd"] for gate in gates_data)

shopifys = [
    "uc",
    "ri",
    "se",
    "ju",
    "bl",
    "be",
    "st",
    "oz",
    "dr",
    "de",
    "ch",
    "ve",
    "hi",
    "sn",
    "kr",
    "as",
    "ha",
    "su",
]

gates_bot = {
    "bo": boruto,
    "dkt": darkito,
    "lynx": lynx,
    "rh": rohee,
    "at": astharoth,
    "ko": ko,
    "ka": ka,
    "ak": stripe_gate,
    "ass": ass,
}

msg_error = "𝙂𝙖𝙩𝙚𝙬𝙖𝙮 𝙈𝙖𝙨𝙨 ♻️\n𝙁𝙤𝙧𝙢𝙖𝙩 -» <code>/ms gate cc|month|year|cvc</code>"


@Client.on_message(filters.command("ms", PREFIXES))
async def mass(client: Client, m: Message):
    user_id = m.from_user.id
    is_premium = False
    with Database() as db:
        user_info = db.get_info_user(user_id)
        is_free_user = user_info["MEMBERSHIP"].lower() == "free user"
        is_premium = db.is_premium(user_id)

    credits = user_info.get("CREDITS", 0)
    if credits < 2:
        return await m.reply("<b>Necesitas más de 2 créditos!</b>", quote=True)
    text = get_text_from_pyrogram(m)
    info_check = text.split(" ", maxsplit=2)
    if len(info_check) < 3:
        return await m.reply(msg_error, quote=True)
    gate = info_check[1]
    gate_check = gates_bot.get(gate, False)
    shopify = False
    if gate_check:
        gate = gate_check
    else:
        if gate in shopifys:
            gate = get_gate_by_cmd(gate, gates_data)
            site = gate["site"]
            shopify = True
            if not site.startswith("https://"):
                site = "https://" + site
            gate = autoshopify
        else:
            return await m.reply(msg_error, quote=True)
    ccs = info_check[2].split("\n")
    ccs_findeds = []
    for cc in ccs:
        cc = get_cc(cc)
        if not cc:
            continue
        card = cc[0]
        resp = await get_bin_info(card[0:6])
        if resp is None:
            continue
        level = resp["level"] if resp["level"] else "UNAVAILABLE"
        typea = resp["type"] if resp["type"] else "UNAVAILABLE"
        banned_bin = resp["banned"]
        if banned_bin or "prepaid" in level.lower() or "prepaid" in typea.lower():
            continue
        if cc in ccs_findeds:
            continue
        ccs_findeds.append(cc)
    if not (0 < len(ccs_findeds) <= 10):
        return await m.reply(msg_error, quote=True)
    if (len(ccs_findeds) * 2) > credits:
        return await m.reply(
            "<b>No puedes verificar esa cantidad de tarjetas con la cantidad de créditos disponibles</b>",
            quote=True,
        )

    ini = perf_counter()
    antispam_result = antispam(user_id, user_info["ANTISPAM"], is_free_user)
    if antispam_result != False:
        return await m.reply(
            f"𝙋𝙡𝙚𝙖𝙨𝙚 𝙒𝙖𝙞𝙩... -» <code>{antispam_result}'s</code>", quote=True
        )
    msg_bot = await m.reply("𝙋𝙡𝙚𝙖𝙨𝙚 𝙒𝙖𝙞𝙩...", quote=True)

    text_ccs = ""
    errors = 0
    approveds = 0
    deads = 0
    for i in range(0, len(ccs_findeds)):
        cc = ccs_findeds[i]
        card = cc[0]
        mes = cc[1]
        ano = cc[2]
        cvv = cc[3]
        ccf = f"{card}|{mes}|{ano}|{cvv}"
        response = None
        status = None

        if shopify:
            response = await handler_gate(
                gate, True, site, card, mes, ano, cvv, is_premium, credits
            )

        else:
            response = await handler_gate(gate, False, card, mes, ano, cvv)
        if not response:
            status = "Error ⚠️"
            msg = "Error ⚠️"
        elif isinstance(response, Exception):
            status = "Error ⚠️"
            msg = "Error ⚠️"
        elif shopify:
            status = response.get("status", "Dead! ❌")
            msg = response["response"]
        elif isinstance(response, tuple) and len(response) == 2:
            status, msg = response
        if "approved" in status.lower():
            approveds += 1
        elif "dead" in status.lower():
            deads += 1
        else:
            errors += 1
        text_ccs += f"""<b>ア 𝘾𝘾 -» <code>{ccf}</code>
カ 𝙎𝙩𝙖𝙩𝙪𝙨 -» <code>{status}</code>
ツ 𝙍𝙚𝙨𝙪𝙡𝙩 -» <code>{msg}</code></b>\n
"""
        await msg_bot.edit(text_ccs)

    rol = user_info["RANK"].capitalize()
    final = perf_counter() - ini
    credits_to_remove = approveds * 2
    approveds = f"Approveds! ✅ -» <code>{approveds}</code>\n" if approveds > 0 else ""
    deads = f"Deads! ❌ -» <code>{deads}</code>\n" if deads > 0 else ""
    errors = f"Error -» <code>{errors}</code> ⚠️\n" if errors > 0 else ""
    with Database() as db:
        db.remove_credits(user_id, credits_to_remove)
        user_info = db.get_info_user(user_id)
    text = f"""<b>{approveds} {deads} {errors}
{text_ccs} ꫟ 𝙏𝙞𝙢𝙚 -» <code>{final:0.4}'s</code>
ツ 𝘾𝙧𝙚𝙙𝙞𝙩𝙨 -» <code>{user_info.get('CREDITS')}</code>
ツ 𝙏𝙤𝙩𝙖𝙡 𝘾𝙖𝙧𝙙𝙨 -» <code>{len(ccs_findeds)}</code>
ᥫ᭡ 𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮 -» <a href='tg://user?id={m.from_user.id}'>{m.from_user.first_name}</a> [{rol}]</b>"""
    await msg_bot.edit(text)
