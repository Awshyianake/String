from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("ꜱᴛᴀᴛʀᴛ ɢᴇɴᴇʀᴀᴛɪɴɢ ꜱᴇꜱꜱɪᴏɴ", callback_data="generate")]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url="https://t.me/getenv"),
         InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴩᴇʀ", url="https://t.me/pyyaml"),
        ],
    ]

    START = """
**Hey** {},

**This is** {},
**Bot untuk Mengambil String Session!**

**Made With 👑 By:** [ιѕυη](https://t.me/pyyaml)
—
**Channel:** [ᴄɪʟɪᴋ ꜱᴜᴘᴘᴏʀᴛ](https://t.me/getenv)
    """
