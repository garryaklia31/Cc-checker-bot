import logging
from os import getenv
from huepy import bad
from pyromod import Client
from pyrogram import filters
from pyrogram.enums import ParseMode, ChatMemberStatus
from pyrogram.types import CallbackQuery, Message
from utilsdf.functions import bot_on
from utilsdf.db import Database
from utilsdf.vars import PREFIXES
    
API_ID = '28386099'
API_HASH = 'a0057fbf1ca49ce5e9d26fd4afd6e78b'
BOT_TOKEN = '6619456557:AAEBZCvlXVv9m0qcoTtJ-Ev7Gs8K-_HnnRI'
CHANNEL_LOGS = '-1001897182152'

app = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="plugins"),
    parse_mode=ParseMode.HTML,
)

bot_on()
logging.basicConfig(level=logging.INFO)
logging.getLogger("httpx").setLevel(logging.CRITICAL)


@app.on_callback_query()
async def warn_user(client: Client, callback_query: CallbackQuery):
    if callback_query.message.reply_to_message.from_user and (
        callback_query.from_user.id
        != callback_query.message.reply_to_message.from_user.id
    ):
        await callback_query.answer("Usa tu menu! ⚠️", show_alert=True)
        return
    await callback_query.continue_propagation()


@app.on_message(filters.text)
async def user_ban(client: Client, m: Message):

    if not m.from_user:
        return
    if not m.text:
        return
    try:
        if not m.text[0] in PREFIXES:
            return
    except UnicodeDecodeError:
        return
    chat_id = m.chat.id
    with Database() as db:
        if chat_id == -1001494650944:
            async for member in m.chat.get_members():
                if not member.user:
                    continue
                if member.status == ChatMemberStatus.ADMINISTRATOR:
                    continue
                user_id = member.user.id
                if db.is_seller_or_admin(user_id):
                    continue
                is_premium = db.is_premium(user_id)
                if is_premium:
                    continue
                if db.user_has_credits(user_id):
                    continue
                await m.chat.ban_member(user_id)
                info=db.get_info_user(user_id)
                await client.send_message(-1001494650944, f"<b>User eliminado: @{info['USERNAME']}</b>")

        #         if not db.is_admin(m.from_user.id):
        #             return await m.reply(
        #                 """𝘽𝙤𝙩 𝙪𝙣𝙙𝙚𝙧 𝙈𝙖𝙣𝙩𝙚𝙣𝙞𝙚𝙣𝙘𝙚 ⚠️
        # 𝙍𝙚𝙖𝙨𝙤𝙣 -» <code>Mantenimiento by @punjab_buy</code>
        #        """
        #             )
        user_id = m.from_user.id
        username = m.from_user.username
        db.remove_expireds_users()
        banned = db.is_ban(user_id)
        if banned:
            return
        db.register_user(user_id, username)
        await m.continue_propagation()


if __name__ == "__main__":
    app.run()
