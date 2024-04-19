import traceback, re, asyncio
from pyrogram import filters
from pyromod import Client
from pyrogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    CallbackQuery,
)
from pyrogram.enums import ParseMode
from utilsdf.db import Database
from utilsdf.functions import (
    anti_bots_telegram,
    get_bin_info,
    get_cc,
    antispam,
    get_text_from_pyrogram,
    user_not_premium,
    random_proxy,
    random_proxy_sh,
)
from utilsdf.vars import PREFIXES
from gates.shopifys import get_response_gate, cmds, get_gate_by_cmd, gates_data
from os import getenv
from dotenv import load_dotenv


load_dotenv("./assets/.env")

button_explication = InlineKeyboardMarkup(
    [[InlineKeyboardButton("Explicacion", "explication")]]
)

info_response_cache = {}
antispam_button = {}

ID_OWNER = getenv("ID_OWNER")


@Client.on_message(filters.command(list(cmds), PREFIXES))
async def shopifys(client: Client, m: Message):
    user_id = m.from_user.id
    cmd = m.command[0]
    gateway = get_gate_by_cmd(cmd, gates_data)
    type_gate = gateway["type"].lower()
    with Database() as db:
        is_premium = db.is_premium(user_id)
        user_info = db.get_info_user(user_id)
        credits = user_info.get("CREDITS", 0)

        if type_gate == "premium":
            if not is_premium:
                await user_not_premium(m)
                return
        elif type_gate == "free":
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
    gateway_name = gateway["gate"]
    # site = gateway["site"]
    text = get_text_from_pyrogram(m)
    ccs = get_cc(text)
    if not ccs:
        return await m.reply(
            f"𝙂𝙖𝙩𝙚𝙬𝙖𝙮 <code>{gateway_name} ♻️</code>\n𝙁𝙤𝙧𝙢𝙖𝙩 -» <code>/{cmd} cc|month|year|cvc</code>",
            quote=True,
        )
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

    # tries = k0
    # while tries < 3:
    #     try:

    max_intentos = 10
    intentos = 0

    result = await get_response_gate(cmd, cc, mes, ano, cvv, is_premium, credits)
    if not result:
        return await msg_to_edit.edit(f"<b>Error!</b>")
    if isinstance(result, Exception):
        e = result

        await client.send_message(
            1115269159,
            f"""Gate: /{cmd}
    {e}
    CC: <code>{cc}|{mes}|{ano}|{cvv}</code>""",
            disable_web_page_preview=True,
        )
        traceback.print_exception(type(e), e, e.__traceback__)
        return await msg_to_edit.edit(f"<b>Error!</b>")

    result = (
        result
        % f"<a href='tg://user?id={m.from_user.id}'>{m.from_user.first_name}</a> []</b>"
    )
    with Database() as db:
        db.increase_checks(user_id)
    await msg_to_edit.edit(result)


# @Client.on_callback_query(filters.regex("explication"))
# async def explication_call(client: Client, callback_query: CallbackQuery):
#     text_bk = callback_query.message.text
#     data = re.search(r"ツ 𝙍𝙚𝙨𝙪𝙡𝙩 -» (.+)", text_bk)
#     data = data.group() if data else "Error"
#     data = data.strip()
#     user_id = callback_query.from_user.id
#     antispam_result = antispam(user_id, 30, times=antispam_button)
#     if antispam_result != False:
#         return await callback_query.answer(f"Espera {antispam_result}'s ⚠️", True)
#     if info_response_cache.get(data, None):
#         response = info_response_cache[data]
#     else:
#         response = await ask_gpt(
#             f"Que significa esta respuesta de un procesador de pagos? {data}",
#             conversation_id,
#         )
#         response = response.get("response", "Error")
#         info_response_cache[data] = response
#     await callback_query.message.reply(
#         f"**{response}**", quote=True, parse_mode=ParseMode.MARKDOWN
#     )
