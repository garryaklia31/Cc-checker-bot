import asyncio
from pyrogram import filters
from pyromod import Client
from pyrogram.types import Message
from utilsdf.db import Database
from utilsdf.functions import (
    get_bin_info_of_database,
    get_cc,
    antispam,
    get_text_from_pyrogram,
    random_proxy_sh,
    get_gate_by_cmd,
    handler_gate,
)
from httpx import AsyncClient
from json import load
from utilsdf.vars import PREFIXES
from time import perf_counter
from utilsdf.gates_for_mass import (
    boruto,
    darkito,
    lynx,
    rohee,
    brenda,
    adriana,
    stripe_gate,
    ass,
    ka,
    ko,
    sebas,
    odali,
    pussy,
    ghoul,
    devilsx,
    astharoth,
    mai,
    autoshopify,
)

with open("assets/gates.json", "r", encoding="utf-8-sig") as json_file:
    gates_data = load(json_file)

cmds = set(gate["cmd"] for gate in gates_data)


shopifys = [
    "bl",
    "ju",
    "mo",
    "st",
    "sn",
    "gu",
    "be",
    "hy",
    "ky",
    "si",
    "su",
    "uc",
    "as",
    "kr",
    "jt",
    "sa",
    "hq",
    "ke",
    "ha",
    "za",
    "ob",
    "ch",
    "ve",
    "de",
    "ri",
    "le",
    "dr",
    "mi",
    "ze",
    "to",
    "da",
    "oz",
]
gates_bot = {
    "mai": mai,
    "bo": boruto,
    "dkt": darkito,
    "lynx": lynx,
    "rh": rohee,
    "at": astharoth,
    "br": brenda,
    "dx": devilsx,
    "ps": pussy,
    "od": odali,
    "sb": sebas,
    "ko": ko,
    "ka": ka,
    "ak": stripe_gate,
    "ass": ass,
    "adr": adriana,
    "gh": ghoul,
}
msg_error = "𝙂𝙖𝙩𝙚𝙬𝙖𝙮 𝙈𝙖𝙨𝙨 ♻️\n𝙁𝙤𝙧𝙢𝙖𝙩 -» <code>/msa gate cc|month|year|cvc</code>"


@Client.on_message(filters.command("msa", PREFIXES))
async def mass_admin(client: Client, m: Message):
    user_id = m.from_user.id
    with Database() as db:
        if not db.is_admin(user_id):
            return
        user_info = db.get_info_user(user_id)
        is_free_user = user_info["MEMBERSHIP"].lower() == "free user"

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
        resp = get_bin_info_of_database(card[0:6])
        if resp is None:
            continue
        if cc in ccs_findeds:
            continue
        ccs_findeds.append(cc)
    if len(ccs_findeds) <= 0:
        return await m.reply(msg_error, quote=True)

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
        async with AsyncClient(
            follow_redirects=True, verify=False, proxies=random_proxy_sh()
        ) as session:
            if shopify:
                response = await handler_gate(
                    gate, True, site, card, mes, ano, cvv, True, 300
                )

            else:
                response = await handler_gate(gate, False, card, mes, ano, cvv)
        if not response:
            status = "Error ⚠️"
            msg = "Error ⚠️"
        elif shopify:
            status = (
                str(response.get("status"))
                if isinstance(response, dict)
                else "Dead! ❌"
            )
            msg = (
                str(response.get("response", "response not available"))
                if isinstance(response, dict)
                else str(response)
            )
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
    approveds = f"Approveds! ✅ -» <code>{approveds}</code>\n" if approveds > 0 else ""
    deads = f"Deads! ❌ -» <code>{deads}</code>\n" if deads > 0 else ""
    errors = f"Error -» <code>{errors}</code> ⚠️\n" if errors > 0 else ""
    with Database() as db:
        user_info = db.get_info_user(user_id)
    text = f"""<b>{approveds} {deads} {errors}
{text_ccs} ꫟ 𝙏𝙞𝙢𝙚 -» <code>{final:0.4}'s</code>
ツ 𝘾𝙧𝙚𝙙𝙞𝙩𝙨 -» <code>{user_info.get('CREDITS')}</code>
ツ 𝙏𝙤𝙩𝙖𝙡 𝘾𝙖𝙧𝙙𝙨 -» <code>{len(ccs_findeds)}</code>
ᥫ᭡ 𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮 -» <a href='tg://user?id={m.from_user.id}'>{m.from_user.first_name}</a> [{rol}]</b>"""

    await msg_bot.edit(text)
