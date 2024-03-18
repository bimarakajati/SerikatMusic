from typing import Union
from config import OWNER_ID, SUPPORT_CHAT, SUPPORT_CHANNEL

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def queue_markup(
    _,
    DURATION,
    CPLAY,
    videoid,
    chat_id,
    played: Union[bool, int] = None,
    dur: Union[bool, int] = None,
):
    not_dur = [
        [
            InlineKeyboardButton(
                text=_["QU_B_1"],
                callback_data=f"GetQueued {CPLAY}|{videoid}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data="close",
            ),
        ],
         [
            InlineKeyboardButton(
                text="🐼 ᴄʜᴀɴɴᴇʟ 🐼", url=SUPPORT_CHANNEL,
                # text="🐼 ᴏᴡɴᴇʀ 🐼", url=f"tg://openmessage?user_id={OWNER_ID}",
            ),
            InlineKeyboardButton(
                text="🐼 ɢʀᴏᴜᴘ 🐼", url=SUPPORT_CHAT,
            ),
        ],
    ]
    dur = [
        [
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="II", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="↻", callback_data=f"ADMIN Replay|{chat_id}"),
            InlineKeyboardButton(text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{chat_id}")
        ],
        [
            InlineKeyboardButton(
                text=_["QU_B_2"].format(played, dur),
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(
                text=_["QU_B_1"],
                callback_data=f"GetQueued {CPLAY}|{videoid}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data="close",
            ),
        ],
         [
            InlineKeyboardButton(
                text="🐼 ᴄʜᴀɴɴᴇʟ 🐼", url=SUPPORT_CHANNEL,
                # text="🐼 ᴏᴡɴᴇʀ 🐼", url=f"tg://openmessage?user_id={OWNER_ID}",
            ),
            InlineKeyboardButton(
                text="🐼 ɢʀᴏᴜᴘ 🐼", url=SUPPORT_CHAT,
            ),
        ],
    ]
    upl = InlineKeyboardMarkup(not_dur if DURATION == "Unknown" else dur)
    return upl


def queue_back_markup(_, CPLAY):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"queue_back_timer {CPLAY}",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                ),
           ],
             [
                InlineKeyboardButton(
                    text="🐼 ᴄʜᴀɴɴᴇʟ 🐼", url=SUPPORT_CHANNEL,
                    # text="🐼 ᴏᴡɴᴇʀ 🐼", url=f"tg://openmessage?user_id={OWNER_ID}",
                ),
                InlineKeyboardButton(
                    text="🐼 ɢʀᴏᴜᴘ 🐼", url=SUPPORT_CHAT,
                ),
            ],
        ]
    )
    return upl


def aq_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(text="▷", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="II", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="‣‣I", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="▢", callback_data=f"ADMIN Stop|{chat_id}"),
        ],
         [
            InlineKeyboardButton(
                text="🐼 ᴄʜᴀɴɴᴇʟ 🐼", url=SUPPORT_CHANNEL,
                # text="🐼 ᴏᴡɴᴇʀ 🐼", url=f"tg://openmessage?user_id={OWNER_ID}",
            ),
            InlineKeyboardButton(
                text="🐼 ɢʀᴏᴜᴘ 🐼", url=SUPPORT_CHAT,
            ),
        ],
    ]
    return buttons
