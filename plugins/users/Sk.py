from pyrogram import filters
from pyromod import Client
from pyrogram.types import Message
from utilsdf.db import Database
from utilsdf.functions import get_info_sk
from utilsdf.vars import PREFIXES
from time import perf_counter


@Client.on_message(filters.command("sk", PREFIXES))
async def sk_cmd(client: Client, m: Message):
    user_id = m.from_user.id
    with Database() as db:
        if not db.is_authorized(user_id, m.chat.id):
            return await m.reply(
                "𝑻𝒉𝒊𝒔 𝒄𝒉𝒂𝒕 𝒊𝒔 𝒏𝒐𝒕 𝒂𝒑𝒑𝒓𝒐𝒗𝒆𝒅 𝒕𝒐 𝒖𝒔𝒆 𝒕𝒉𝒊𝒔 𝒃𝒐𝒕.", quote=True
            )
        info_user = db.get_info_user(user_id)
    ini = perf_counter()
    sk_key = m.text[len(m.command[0]) + 2 :].strip()
    if not sk_key:
        return await m.reply("𝙎𝙠 ♻️\n𝙁𝙤𝙧𝙢𝙖𝙩 -» <code>/sk sk_live...</code>", quote=True)
    if not sk_key.startswith("sk_live_"):
        return await m.reply("𝙄𝙣𝙫𝙖𝙡𝙞𝙙 𝙎𝙠 ⚠️", quote=True)
    result = await get_info_sk(sk_key)
    status = "Sk Live! ✅"
    result_msg = "Success"
    if not "available" in result:
        status = "Dead! ❌"
        result_msg = result["error"]["message"]

    text = f"""ア 𝙎𝙠 -» <code>{sk_key}</code>

カ 𝙎𝙩𝙖𝙩𝙪𝙨 -» <code>{status}</code>
ツ 𝙍𝙚𝙨𝙪𝙡𝙩 -» <code>{result_msg}</code>"""

    if "available" in result:
        availableAmount = result["available"][0]["amount"]
        availableCurrency = result["available"][0]["currency"]
        pendingAmount = result["pending"][0]["amount"]
        pendingCurrency = result["pending"][0]["currency"]
        text += f"""\n
𝘼𝙢𝙤𝙪𝙣𝙩 -» <code>{availableAmount} {availableCurrency}</code>
𝙋𝙚𝙣𝙙𝙞𝙣𝙜 -» <code>{pendingAmount} {pendingCurrency}</code>\n"""
    final = perf_counter() - ini
    text += f"""
꫟ 𝙏𝙞𝙢𝙚 -» <code>{final:0.1}'s</code>
ᥫ᭡ 𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮 -» <a href='tg://user?id={m.from_user.id}'>{m.from_user.first_name}</a> [{info_user["RANK"].capitalize()}]"""

    text = f"<b>{text}</b>"
    await m.reply(text, quote=True)
