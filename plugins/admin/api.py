import traceback
from gates.autosh import autoshopify
from httpx import AsyncClient
from pyrogram import filters
from pyromod import Client
from pyrogram.types import Message
from utilsdf.db import Database
from utilsdf.vars import PREFIXES
from utilsdf.functions import antispam, random_proxy


@Client.on_message(filters.command("api", PREFIXES))
async def api(client: Client, m: Message):
    user_id = m.from_user.id
    with Database() as db:
        if not db.is_admin(user_id):
            return
        user_info = db.get_info_user(user_id)
    url = str(m.text[len(m.command[0]) + 2 :].strip())
    if url.startswith("http://"):
        url.replace("http://", "https://")
    if not url.startswith("https://"):
        url = "https://" + url
    if not url or not url_validator(url):
        return await m.reply("<b>Ingresa una url valida!</b>", quote=True)
    antispam_result = antispam(user_id, user_info["ANTISPAM"])
    if antispam_result != False:
        return await m.reply(
            f"𝙋𝙡𝙚𝙖𝙨𝙚 𝙒𝙖𝙞𝙩... -» <code>{antispam_result}'s</code>", quote=True
        )
    msg = await m.reply("𝙋𝙡𝙚𝙖𝙨𝙚 𝙒𝙖𝙞𝙩...", quote=True)
    try:

        response = await autoshopify(
            url, "4108435545380660", "10", "2024", "666", True, 20
        )
    except Exception as e:
        message = "Graphql" if "graphql" in str(e) else "Error"
        traceback.print_exception(type(e), e, e.__traceback__)
        return await msg.edit(
            f"""<b>{message}!</b> ᥫ᭡ 𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮 -» <a href='tg://user?id={m.from_user.id}'>
            {m.from_user.first_name}</a>"""
        )
    if not response:
        return await msg.edit("<b>Error!</b>\nResponse not found")
    site = response["site"]
    status = response["status"]
    response_site = response["response"]
    time = response["time"]
    total = response["total"]
    await msg.edit(
        f"""<b>
ツ 𝙎𝙞𝙩𝙚 -» <code>{site}</code>
ツ 𝙋𝙧𝙞𝙘𝙚 -» <code>{total[:2]}$</code>

カ 𝙎𝙩𝙖𝙩𝙪𝙨 -» <code>{status}</code>
ツ 𝙍𝙚𝙨𝙪𝙡𝙩 -» <code>{response_site}</code>

⸙ 𝙂𝙖𝙩𝙚𝙬𝙖𝙮 -» 𝘼𝙥𝙞 ♻️
꫟ 𝙏𝙞𝙢𝙚 -» <code>{time}'s</code>
ᥫ᭡ 𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮 -» <a href='tg://user?id={m.from_user.id}'>{m.from_user.first_name}</a></b>"""
    )
