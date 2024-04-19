from pyrogram import filters
from pyromod import Client
from pyrogram.types import Message
from utilsdf.vars import PREFIXES
from utilsdf.db import Database
from os import getenv


CHANNEL_REFES = getenv("CHANNEL_OFFICIAL")

INVALID_REFE = "<b>Debes responder a una referencia valida</b>"


@Client.on_message(filters.command("refer", PREFIXES))
async def refer(client: Client, m: Message):
    user_id = m.from_user.id
    with Database() as db:
        if not db.is_seller_or_admin(user_id):
            return
    message = m.reply_to_message
    if not message or not message.media:
        return await m.reply(INVALID_REFE, quote=True)

    await client.forward_messages(CHANNEL_REFES, m.chat.id, message.id)
    await m.reply("𝙍𝙚𝙛𝙚𝙧𝙚𝙣𝙘𝙚 𝙎𝙚𝙣𝙙", reply_to_message_id=message.id)
