#  Moon-Userbot - telegram userbot
#  Copyright (C) 2020-present Moon Userbot Organization
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.

#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.

#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.


@Client.on_message(
    filters.command(["ping"], ".") & (filters.me | filters.user(SUDO_USER))
)
async def pingme(client: Client, message: Message):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    xx = await message.reply_text("**0% ▒▒▒▒▒▒▒▒▒▒**")
    try:
       await message.delete()
    except:
       pass
    await xx.edit("**20% ██▒▒▒▒▒▒▒▒ 🚩😈ᴘᴏɪsᴏɴ ᴏᴘ ʙᴏʟᴛᴇ🚩😈**")
    await xx.edit("**40% ████▒▒▒▒▒▒ 🚩😈ᴊᴀɪ sʜʀᴇᴇ ʀᴀᴍ**")
    await xx.edit("**60% ██████▒▒▒▒ 🚩😈ʀᴀᴅʜᴇ ᴋʀɪsʜɴᴀ**")
    await xx.edit("**80% ████████▒▒ 🚩😈Hᴀʀ ʜᴀʀ ᴍᴀʜᴀᴅᴇᴠ**")
    await xx.edit("**100% ████████▒▒ 🚩Jᴀɪ sʜʀᴇᴇ ʀᴀᴍ🚩**")
    end = datetime.now()
    duration = (end - start).microseconds / 100
    await xx.edit(
        f"🚩🕉️ **🔥🖤ᴘᴏɪsᴏɴ ᴛᴏxɪᴄ ᴅᴏ ᴅɪʟ ᴇᴋ ᴊᴀᴀɴ🔥🖤**\n"
        f"❏ **🚩😈ᴘᴏɪsᴏɴ ʙᴏᴛ ғɪʀᴇ ᴏɴ😈🚩**\n"
        f"├• **🚩🕉️** - `%sms`\n"
        f"├• **🚩🕉️ -** `{uptime}` \n"
        f"└• **🚩🕉️:** {client.me.mention}" % (duration)
    )


add_command_help(
    "ping",
    [
        ["ping", "Check bot alive or not."],
    ],
)
