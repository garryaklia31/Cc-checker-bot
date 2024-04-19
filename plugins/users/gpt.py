# from pyrogram import filters
# from pyromod import Client
# from pyrogram.enums import ParseMode
# from pyrogram.types import Message
# from utils.db import Database
# from utils.functions import ask_gpt, user_not_premium, antispam
# from utils.vars import PREFIXES


# @Client.on_message(filters.command("gpt", PREFIXES))
# async def chat_gpt(client: Client, m: Message):
#     user_id = m.from_user.id
#     with Database() as db:
#         if not db.IsPremium(user_id):
#             await user_not_premium(m)
#             return
#         user_info = db.GetInfoUser(user_id)
#     antispam_user = user_info.get("ANTISPAM")
#     antispam_result = antispam(user_id, limit=antispam_user, free_user=False)
#     if antispam_result != False:
#         return await m.reply(
#             f"𝙋𝙡𝙚𝙖𝙨𝙚 𝙒𝙖𝙞𝙩... -» <code>{antispam_result}'s</code>", quote=True
#         )
#     ask = m.text[len(m.command[0]) + 2 :].strip()
#     if len(ask) < 3:
#         return await m.reply("<b>Ingresa una pregunta valida</b>", quote=True)
#     gpt_id = user_info.get("GPTID", None)
#     response = await ask_gpt(ask, gpt_id)
#     with Database() as db:
#         db.UpdateColumn(user_id, "GPTID", response["conversation_id"])
#     response = response["response"]
#     await m.reply(f"**{response}**", quote=True, parse_mode=ParseMode.MARKDOWN)
