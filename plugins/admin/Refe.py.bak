from pyrogram import filters
from pyromod import Client
from pyrogram.types import Message
from utilsdf.vars import PREFIXES
from dotenv import load_dotenv
from os import getenv

load_dotenv("./assets/.env")

REFES_CHAT = getenv("REFES_CHAT")

INVALID_REFE = "<b>Debes responder a una referencia valida</b>"


@Client.on_message(filters.command("refe", PREFIXES))
async def refe(client: Client, m: Message):
    message = m.reply_to_message
    if not message or not message.media:
        return await m.reply(INVALID_REFE, quote=True)

    await client.forward_messages(REFES_CHAT, m.chat.id, message.id)
    await m.reply("𝙍𝙚𝙛𝙚𝙧𝙚𝙣𝙘𝙚 𝙪𝙣𝙙𝙚𝙧 𝙧𝙚𝙫𝙞𝙚𝙬", reply_to_message_id=message.id)
