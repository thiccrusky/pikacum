# Credits: @mrismanaziz
# FROM File-Sharing-Man <https://github.com/mrismanaziz/File-Sharing-Man/>
# t.me/SharingUserbot & t.me/Lunatic0de

from config import FORCE_SUB_CHANNEL, FORCE_SUB_GROUP
from pyrogram.types import InlineKeyboardButton


def start_button(client):
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="𝐎𝐑𝐃𝐄𝐑 𝐕𝐕𝐈𝐏", url=f"https://t.me/CumAgent"),
                InlineKeyboardButton(text="𝐓𝐔𝐓𝐔𝐏", callback_data="close"),
            ],
        ]
        return buttons


def fsub_button(client,message):
    if FORCE_SUB_CHANNEL and FORCE_SUB_GROUP:
        buttons = [
            [
                InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ", url=client.invitelink),
                InlineKeyboardButton(text="ᴊᴏɪɴ ɢʀᴏᴜᴘ", url=client.invitelink2),
            ],
        ]
        try:
            buttons.append(
                [
                    InlineKeyboardButton(
                        text="ᴄᴏʙᴀ ʟᴀɢɪ",
                        url=f"https://t.me/{client.username}?start={message.command[1]}",
                    )
                ]
            )
        except IndexError:
            pass
        return buttons
