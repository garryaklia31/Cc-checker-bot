from pyrogram import filters
from pyromod import Client
from pyrogram.types import (
    Message,
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from utilsdf.db import Database
from utilsdf.functions import get_bin_info
from re import search
from random import randint
from utilsdf.vars import PREFIXES

buttons = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("𝙍𝙚-𝙂𝙚𝙣 🔄", callback_data="regen-bin")],
        [InlineKeyboardButton("𝙀𝙭𝙞𝙩 ⚠", callback_data="exit")],
    ]
)

not_autorized = "𝑻𝒉𝒊𝒔 𝒄𝒉𝒂𝒕 𝒊𝒔 𝒏𝒐𝒕 𝒂𝒑𝒑𝒓𝒐𝒗𝒆𝒅 𝒕𝒐 𝒖𝒔𝒆 𝒕𝒉𝒊𝒔 𝒃𝒐𝒕."


@Client.on_message(filters.command("gbin", PREFIXES))
async def gbin(client: Client, m: Message):
    user_id = m.from_user.id
    first_name = m.from_user.first_name
    with Database() as db:
        if not db.is_authorized(user_id, m.chat.id):
            return await m.reply(not_autorized, quote=True)
        user_info = db.get_info_user(user_id)
    text = m.text[len(m.command[0]) + 2 :].strip()
    rands_bins_info = await get_rand_bin_info(
        text, user_id, first_name, user_info["RANK"]
    )
    if not rands_bins_info:
        return await m.reply(
            """System Akatsuki -»>_

𝙎𝙚𝙚𝙙 -» Invalid! ⚠
        ️"""
        )
    await m.reply(rands_bins_info, quote=True, reply_markup=buttons)


@Client.on_callback_query(filters.regex("regen-bin"))
async def regen_call(client: Client, callback_query: CallbackQuery):
    text = callback_query.message.text
    data = search(r"\d+", text).group()
    user_id = callback_query.from_user.id
    first_name = callback_query.from_user.first_name
    with Database() as db:
        user_info = db.get_info_user(user_id)
    rands_bins_info = await get_rand_bin_info(
        data, user_id, first_name, user_info["RANK"]
    )
    await callback_query.edit_message_text(rands_bins_info, reply_markup=buttons)


async def get_rand_bin_info(
    seed, user_id, first_name, rol, quantity: int = 3
) -> str | bool:
    if (
        len(seed) not in range(1, 6)
        or not seed.isdigit()
        or seed[0] not in ["3", "4", "5", "6"]
    ):
        return False

    bins_info = f"""𝙎𝙚𝙚𝙙 -» <code>{seed.ljust(6, "x")}</code>
- - - - - - - - - - - - - - - - - - - - -"""
    for _ in range(quantity):
        bin_to_format = seed + "".join(str(randint(1, 9)) for _ in range(5))
        resp = None
        while True:
            resp = await get_bin_info(bin_to_format)
            if resp is not None:
                break
            bin_to_format = seed + "".join(str(randint(1, 9)) for _ in range(5))
        brand, level, typea = (
            resp["brand"] or "UNAVAILABLE",
            resp["level"] or "UNAVAILABLE",
            resp["type"] or "UNAVAILABLE",
        )
        country_name, country_flag, bank = (
            resp["country_name"],
            resp["country_flag"],
            resp["bank"],
        )
        bins_info += f"""\n𝘽𝙞𝙣 -» <code>{bin_to_format}</code>
𝙄𝙣𝙛𝙤 -» <code>{brand}</code> - <code>{typea}</code> - <code>{level}</code>
𝘽𝙖𝙣𝙠 -» <code>{bank}</code>
𝘾𝙤𝙪𝙣𝙩𝙧𝙞𝙚𝙨 -» <code>{country_name}</code> {country_flag}
- - - - - - - - - - - - - - - - - - - - -"""

    bins_info += f"\n𝙂𝙚𝙣 𝙗𝙮 -» <a href='tg://user?id={user_id}'>{first_name}</a> -» <code>{rol.capitalize()}</code>"
    return bins_info
