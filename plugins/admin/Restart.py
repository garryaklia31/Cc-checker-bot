# import os, sys
# from utils.db import Database
# from asyncio import sleep
# from pyrogram import filters
from pyromod import Client

# from pyrogram.types import Message
# from utils.vars import PREFIXES


# @Client.on_message(filters.command("rbot", PREFIXES))
# async def rbot(client: Client, m: Message):
#     with Database() as db:
#         if not db.IsAdmin(m.from_user.id):
#             return
#     m1 = await m.reply("<b>Reiniciando bot...</b>", quote=True)
#     await sleep(1.5)
#     await m1.edit("<b>Bot reiniciado ✅ Espere 3 segundos</b>")
#     os.execl(sys.executable, sys.executable, "-B", *sys.argv)
