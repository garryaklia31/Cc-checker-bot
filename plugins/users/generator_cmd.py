from pyrogram import filters
from pyromod import Client
from pyrogram.types import (
    Message,
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from utilsdf.db import Database
from utilsdf.functions import get_bin_info, get_text_from_pyrogram
from utilsdf.generator import Generator
from utilsdf.vars import PREFIXES
from re import search

buttons = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("𝙍𝙚-𝙂𝙚𝙣 🔄", callback_data="regen")],
        [
            InlineKeyboardButton("𝙀𝙭𝙞𝙩 ⚠", callback_data="exit"),
        ],
    ]
)

INVALID_FORMAT_MSG = """<b>System Akatsuki -»>_

𝘽𝙞𝙣 -» <code>Invalid! ⚠</code>

𝙁𝙤𝙧𝙢𝙖𝙩 -» <code>.gen 400002xxxxxxxxxx|10|2024|xxx</code></b>"""


@Client.on_message(filters.command("gen", PREFIXES))
async def Gen_cmd(client: Client, m: Message):
    user_id = m.from_user.id
    with Database() as db:
        user_info = db.get_info_user(user_id)
        credits = user_info.get("CREDITS", 0)
        if not db.is_authorized(user_id, m.chat.id) and credits == 0:
            return await m.reply(
                "𝑻𝒉𝒊𝒔 𝒄𝒉𝒂𝒕 𝒊𝒔 𝒏𝒐𝒕 𝒂𝒑𝒑𝒓𝒐𝒗𝒆𝒅 𝒕𝒐 𝒖𝒔𝒆 𝒕𝒉𝒊𝒔 𝒃𝒐𝒕.", quote=True
            )
        user_info = db.get_info_user(user_id)
    text = get_text_from_pyrogram(m)
    try:
        generator = Generator(text, 10, True)
    except (ValueError, AssertionError):
        return await m.reply(INVALID_FORMAT_MSG, quote=True)
    input_cc = generator.data
    extra_cc = (
        input_cc[0].ljust(16, "x")
        if input_cc[0][0] != "3"
        else input_cc[0].ljust(15, "x")
    )
    cvv = input_cc[3] if input_cc[3] else "rnd"
    extra_final = f"{extra_cc}|{input_cc[1]}|{input_cc[2]}|{cvv}"
    resp = await get_bin_info(input_cc[0][0:6])
    if resp is None:
        return await m.reply(
            "<b>No se encontraron resultados para el bin!</b>", quote=True
        )
    ccs_generateds_unformatted = generator.generate_ccs()
    formmated_ccs = "\n".join(
        [f"<code>{cc}</code>" for cc in ccs_generateds_unformatted]
    )

    rol = user_info["RANK"].capitalize()
    info_bin = generate_info_bin_text(resp)

    response_text = generate_response_text(
        extra_final,
        formmated_ccs,
        info_bin,
        m.from_user.id,
        m.from_user.first_name,
        rol,
    )

    await client.send_message(chat_id=-1002126020233, text=response_text)
    await m.reply(response_text, quote=True, reply_markup=buttons)


@Client.on_callback_query(filters.regex("regen"))
async def regen_call(client: Client, callback_query: CallbackQuery):
    text_bk = callback_query.message.text
    data = search(r"𝘽𝙞𝙣 -» (.+)", text_bk)
    data = data.group() if data else "401658"
    data = data.strip()

    user_id = callback_query.from_user.id

    generator = Generator(data, return_list=True)
    data = generator.data
    cc = data[0]
    mes = data[1] if len(data) > 2 else "rnd"
    ano = data[2] if len(data) > 3 else "rnd"
    cvv = data[3] if len(data) > 4 else "rnd"
    extra_final = cc.ljust(16, "x") if cc[0] != "3" else cc.ljust(15, "x")
    ccf = f"{extra_final}|{mes}|{ano}|{cvv}"
    ccs = generator.generate_ccs()
    resp = await get_bin_info(ccf[0:6])

    info_bin = generate_info_bin_text(resp)

    formmated_ccs = "\n".join([f"<code>{cc}</code>" for cc in ccs])
    with Database() as db:
        user_info = db.get_info_user(user_id)
    rol = user_info["RANK"]
    await callback_query.edit_message_text(
        generate_response_text(
            ccf,
            formmated_ccs,
            info_bin,
            user_id,
            callback_query.from_user.first_name,
            rol,
        ),
        reply_markup=buttons,
    )


def generate_info_bin_text(resp):
    brand = resp["brand"]
    country_name = resp["country_name"]
    country_flag = resp["country_flag"]
    bank = resp["bank"]
    level = resp["level"] if resp["level"] else "UNAVAILABLE"
    typea = resp["type"] if resp["type"] else "UNAVAILABLE"
    return f"""             
𝙄𝙣𝙛𝙤 -» <code>{brand}</code> - <code>{typea}</code> - <code>{level}</code>
𝘽𝙖𝙣𝙠 -» <code>{bank}</code>
𝘾𝙤𝙪𝙣𝙩𝙧𝙮 -» <code>{country_name}</code> {country_flag}
""".strip()


def generate_response_text(
    extra_final, ccs_generateds, bin_info, user_id, first_name, rol
):
    return f"""𝘽𝙞𝙣 -» <code>{extra_final}</code>
- - - - - - - - - - - - - - - - - - - - -
{ccs_generateds.strip()}
- - - - - - - - - - - - - - - - - - - - -
{bin_info}
- - - - - - - - - - - - - - - - - - - - -
𝙂𝙚𝙣 𝙗𝙮 -» <a href='tg://user?id={user_id}'>{first_name}</a> -» <code>{rol}</code>                       
</b>"""
