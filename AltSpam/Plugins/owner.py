import os
import asyncio
import shutil
import dotenv
import urllib3
import config
from git import Repo
from pyrogram import filters, Client
from pyrogram.types import Message
from datetime import datetime
from config import OWNER_ID
from AltSpam.Helpers import Pastebin
from git.exc import GitCommandError, InvalidGitRepositoryError


__NAME__ = "Oᴡɴᴇʀ"
__HELP__ = """
⊱ `usage` : sʜᴏᴡs ᴛʜᴇ ᴅʏɴᴏ ᴜsᴀɢᴇ ᴏғ ᴛʜᴇ ᴍᴏɴᴛʜ.

⊱ `getvar [ᴠᴀʀ ɴᴀᴍᴇ] [ᴠᴀʟᴜᴇ]` : ɢᴇᴛ ᴀ ᴄᴏɴғɪɢ ᴠᴀʀ ғʀᴏᴍ ʜᴇʀᴏᴋᴜ ᴏʀ .ᴇɴᴠ

⊱ `delvar [ᴠᴀʀ ɴᴀᴍᴇ] [ᴠᴀʟᴜᴇ]` : ᴅᴇʟᴇᴛᴇ ᴀ ᴄᴏɴғɪɢ ᴠᴀʀ ᴏɴ ʜᴇʀᴏᴋᴜ ᴏʀ .ᴇɴᴠ

⊱ `setvar [ᴠᴀʀ ɴᴀᴍᴇ] [ᴠᴀʟᴜᴇ]` : sᴇᴛ ᴏʀ ᴜᴩᴅᴀᴛᴇ ᴀ ᴄᴏɴғɪɢ ᴠᴀʀ ᴏɴ ʜᴇʀᴏᴋᴜ ᴏʀ .ᴇɴᴠ

⊱ `reboot` : ʀᴇʙᴏᴏᴛ ʏᴏᴜʀ ʙᴏᴛ

⊱ `update` : ᴜᴩᴅᴀᴛᴇ ᴛʜᴇ ʙᴏᴛ ғʀᴏᴍ ᴛʜᴇ ᴜᴩsᴛʀᴇᴀᴍ ʀᴇᴩᴏ

⊱ `logs` : ɢᴇᴛ ʟᴏɢs ᴏғ ʏᴏᴜʀ ʙᴏᴛ 
"""


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


@Client.on_message(filters.command(["logs", "getlog", "log"], ["/", ".", "!"]) & filters.user(OWNER_ID))
async def log_(_, message: Message):
    try:
        await message.delete()
    except:
        pass

    if os.path.exists("logs.txt"):
        log = open("logs.txt")
        lines = log.readlines()
        data = ""
        try:
            NUMB = int(message.text.split(None, 1)[1])
        except:
            NUMB = 100
        for x in lines[-NUMB:]:
            data += x
        link = await Pastebin(data)
        if link:
            return await message.reply_text(link)
        else:
            await message.reply_document("logs.txt")
    else:
        return await message.reply_text("something went wrong !")


@Client.on_message(filters.command(["getvar"], ["/", ".", "!"]) & filters.user(OWNER_ID) & ~filters.forwarded)
async def varget_(_, message: Message):
    try:
        await message.delete()
    except:
        pass
    usage = "**ᴜsᴀɢᴇ:**\n/getvar [ᴠᴀʀ-ɴᴀᴍᴇ]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    check_var = message.text.split(None, 2)[1]
    
    path = dotenv.find_dotenv()
    if not path:
        return await message.reply_text(".ᴇɴᴠ ꜰɪʟᴇ ɴᴏᴛ ꜰᴏᴜɴᴅ.")
    output = dotenv.get_key(path, check_var)
    if not output:
        await message.reply_text("ᴜɴᴀʙʟᴇ ᴛᴏ ꜰɪɴᴅ ᴀɴʏ sᴜᴄʜ ᴠᴀʀ.")
    else:
        return await message.reply_text(f"**{check_var}:** `{str(output)}`")


@Client.on_message(filters.command(["delvar"], ["/", ".", "!"]) & filters.user(OWNER_ID) & ~filters.forwarded)
async def vardel_(_, message: Message):
    try:
        await message.delete()
    except:
        pass
    usage = "**ᴜsᴀɢᴇ:**\n/delvar [ᴠᴀʀ-ɴᴀᴍᴇ]"
    if len(message.command) != 2:
        return await message.reply_text(usage)
    check_var = message.text.split(None, 2)[1]
    
    path = dotenv.find_dotenv()
    if not path:
        return await message.reply_text(".ᴇɴᴠ ꜰɪʟᴇ ɴᴏᴛ ꜰᴏᴜɴᴅ.")
    output = dotenv.unset_key(path, check_var)
    if not output[0]:
        return await message.reply_text("ᴜɴᴀʙʟᴇ ᴛᴏ ꜰɪɴᴅ ᴀɴʏ sᴜᴄʜ ᴠᴀʀ.")
    else:
        await message.reply_text("{0} ᴅᴇʟᴇᴛᴇᴅ.".format(check_var))
        os.system(f"kill -9 {os.getpid()} && python3 -m AltSpam")


@Client.on_message(filters.command(["setvar"], ["/", ".", "!"]) & filters.user(OWNER_ID) & ~filters.forwarded)
async def set_var(_, message: Message):
    try:
        await message.delete()
    except:
        pass
    usage = "**ᴜsᴀɢᴇ:**\n/setvar [ᴠᴀʀ-ɴᴀᴍᴇ] [ᴠᴀʀ-ᴠᴀʟᴜᴇ]"
    if len(message.command) < 3:
        return await message.reply_text(usage)
    to_set = message.text.split(None, 2)[1].strip()
    value = message.text.split(None, 2)[2].strip()
    
    path = dotenv.find_dotenv()
    if not path:
        return await message.reply_text(".ᴇɴᴠ ꜰɪʟᴇ ɴᴏᴛ ꜰᴏᴜɴᴅ.")
    dotenv.set_key(path, to_set, value)
    if dotenv.get_key(path, to_set):
        await message.reply_text("{0} ʜᴀs ʙᴇᴇɴ ᴜᴘᴅᴀᴛᴇᴅ sᴜᴄᴄᴇssꜰᴜʟʟʏ.".format(to_set))
    else:
        await message.reply_text("{0} ʜᴀs ʙᴇᴇɴ ᴀᴅᴅᴇᴅ sᴜᴄᴄᴇssꜰᴜʟʟʏ.".format(to_set))
    os.system(f"kill -9 {os.getpid()} && python3 -m AltSpam")




@Client.on_message(filters.command(["update", "gitpull"], ["/", ".", "!"]) & filters.user(OWNER_ID) & ~filters.forwarded)
async def update_(_, message: Message):
    try:
        await message.delete()
    except:
        pass
    response = await message.reply_text("ᴄʜᴇᴄᴋɪɴɢ ꜰᴏʀ ᴀᴠᴀɪʟᴀʙʟᴇ ᴜᴘᴅᴀᴛᴇs...")
    try:
        repo = Repo()
    except GitCommandError:
        return await response.edit("ɢɪᴛ ᴄᴏᴍᴍᴀɴᴅ ᴇʀʀᴏʀ !")
    except InvalidGitRepositoryError:
        return await response.edit("ɪɴᴠᴀʟɪᴅ ɢɪᴛ ʀᴇᴘosɪᴛᴏʀʏ !")
    to_exc = f"git fetch origin {config.UPSTREAM_BRANCH} &> /dev/null"
    os.system(to_exc)
    await asyncio.sleep(7)
    verification = ""
    REPO_ = repo.remotes.origin.url.split(".git")[0]  # main git repository

    for checks in repo.iter_commits(f"HEAD..origin/{config.UPSTREAM_BRANCH}"):
        verification = str(checks.count())
    if verification == "":
        return await response.edit("ʙᴏᴛ ɪs ᴜᴩ-ᴛᴏ-ᴅᴀᴛᴇ ᴡɪᴛʜ ᴜᴩsᴛʀᴇᴀᴍ ʀᴇᴩᴏ !")
    updates = ""
    ordinal = lambda format: "%d%s" % (
        format,
        "tsnrhtdd"[
            (format // 10 % 10 != 1)
            * (format % 10 < 4)
            * format
            % 10 :: 4
        ],
    )
    for info in repo.iter_commits(f"HEAD..origin/{config.UPSTREAM_BRANCH}"):
        updates += f"<b>➣ #{info.count()}: [{info.summary}]({REPO_}/commit/{info}) by -> {info.author}</b>\n\t\t\t\t<b>➥ ᴄᴏᴍᴍɪᴛᴇᴅ ᴏɴ:</b> {ordinal(int(datetime.fromtimestamp(info.committed_date).strftime('%d')))} {datetime.fromtimestamp(info.committed_date).strftime('%b')}, {datetime.fromtimestamp(info.committed_date).strftime('%Y')}\n\n"
    
    _update_response_ = "<b>ᴀ ɴᴇᴡ ᴜᴩᴅᴀᴛᴇ ɪs ᴀᴠᴀɪʟᴀʙʟᴇ ғᴏʀ ᴛʜᴇ ʙᴏᴛ !</b>\n\n➣ ᴩᴜsʜɪɴɢ ᴜᴩᴅᴀᴛᴇs ɴᴏᴡ</code>\n\n**<u>ᴜᴩᴅᴀᴛᴇs:</u>**\n\n"
    _final_updates_ = _update_response_ + updates

    if len(_final_updates_) > 4096:
        url = await Pastebin(updates)
        nrs = await response.edit(
            f"<b>ᴀ ɴᴇᴡ ᴜᴩᴅᴀᴛᴇ ɪs ᴀᴠᴀɪʟᴀʙʟᴇ ғᴏʀ ᴛʜᴇ ʙᴏᴛ !</b>\n\n➣ ᴩᴜsʜɪɴɢ ᴜᴩᴅᴀᴛᴇs ɴᴏᴡ</code>\n\n**<u>ᴜᴩᴅᴀᴛᴇs:</u>**\n\n[ᴄʜᴇᴄᴋ ᴜᴩᴅᴀᴛᴇs]({url})"
        )
    else:
        nrs = await response.edit(_final_updates_, disable_web_page_preview=True)

    os.system("git stash &> /dev/null && git pull")

    await response.edit(f"{nrs.text}\n\nʙᴏᴛ ᴜᴩᴅᴀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ ! ɴᴏᴡ ᴡᴀɪᴛ ғᴏʀ ғᴇᴡ ᴍɪɴᴜᴛᴇs ᴜɴᴛɪʟ ᴛʜᴇ ʙᴏᴛ ʀᴇsᴛᴀʀᴛs ᴀɴᴅ ᴩᴜsʜ ᴄʜᴀɴɢᴇs !")
    os.system("pip3 install -r requirements.txt")
    os.system(f"kill -9 {os.getpid()} && python3 -m AltSpam")
    exit()


@Client.on_message(filters.command(["reboot"], ["/", ".", "!"]) & filters.user(OWNER_ID) & ~filters.forwarded)
async def reboot_(_, message: Message):
    try:
        await message.delete()
    except:
        pass
    response = await message.reply_text("ʀᴇsᴛᴀʀᴛɪɴɢ...")
    try:
        shutil.rmtree("downloads")
        shutil.rmtree("raw_files")
        shutil.rmtree("cache")
    except:
        pass
    await response.edit_text("ʀᴇsᴛᴀʀᴛ ᴩʀᴏᴄᴇss sᴛᴀʀᴛᴇᴅ sᴜᴄᴄᴇssғᴜʟʟʏ, ᴡᴀɪᴛ ғᴏʀ ғᴇᴡ ᴍɪɴᴜᴛᴇs ᴜɴᴛɪʟ ᴛʜᴇ ʙᴏᴛ ʀᴇsᴛᴀʀᴛs.")
    os.system(f"kill -9 {os.getpid()} && python3 -m AltSpam")
