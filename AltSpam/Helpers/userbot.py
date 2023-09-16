import config
from pyrogram import Client
from AltSpam.logging import LOGGER



if config.SESSION1:
    one = Client(name="AltSpam1", api_id=config.API_ID, api_hash=config.API_HASH, session_string=str(config.SESSION1), plugins=dict(root="AltSpam.Plugins"))
else:
    one = None
    
if config.SESSION2:
    two = Client(name="AltSpam2", api_id=config.API_ID, api_hash=config.API_HASH, session_string=str(config.SESSION2), plugins=dict(root="AltSpam.Plugins"))
else:
    two = None
    
if config.SESSION3:
    three = Client(name="AltSpam3", api_id=config.API_ID, api_hash=config.API_HASH, session_string=str(config.SESSION3), plugins=dict(root="AltSpam.Plugins"))
else:
    three = None
    
if config.SESSION4:
    four = Client(name="AltSpam4", api_id=config.API_ID, api_hash=config.API_HASH, session_string=str(config.SESSION4), plugins=dict(root="AltSpam.Plugins"))
else:
    four = None

if config.SESSION5:
    five = Client(name="AltSpam5", api_id=config.API_ID, api_hash=config.API_HASH, session_string=str(config.SESSION5), plugins=dict(root="AltSpam.Plugins"))
else:
    five = None
    
    
async def userbot():
    if config.SESSION1:
        await one.start()
        get_me1 = await one.get_me()
        alt1 = get_me1.id
        config.SUDO_USERS.append(alt1)
        try:
            await one.join_chat("TeamSirion")
            await one.join_chat("TheAltron")
            await one.join_chat("AltronChats")
            await one.join_chat("AltSpam")
        except:
            pass
        LOGGER("AltSpam").info("AltSpam One Started !")

    if config.SESSION2:
        await two.start()
        get_me2 = await two.get_me()
        alt2 = get_me2.id
        config.SUDO_USERS.append(alt2)
        try:
            await two.join_chat("TeamSirion")
            await two.join_chat("TheAltron")
            await two.join_chat("AltronChats")
            await two.join_chat("AltSpam")
        except:
            pass
        LOGGER("AltSpam").info("AltSpam Two Started !")
            
    if config.SESSION3:
        await three.start()
        get_me3 = await three.get_me()
        alt3 = get_me3.id
        config.SUDO_USERS.append(alt3)
        try:
            await three.join_chat("TeamSirion")
            await three.join_chat("TheAltron")
            await three.join_chat("AltronChats")
            await three.join_chat("AltSpam")
        except:
            pass
        LOGGER("AltSpam").info("AltSpam Three Started !")

    if config.SESSION4:
        await four.start()
        get_me4 = await four.get_me()
        alt4 = get_me4.id
        config.SUDO_USERS.append(alt4)
        try:
            await four.join_chat("TeamSirion")
            await four.join_chat("TheAltron")
            await four.join_chat("AltronChats")
            await four.join_chat("AltSpam")
        except:
            pass
        LOGGER("AltSpam").info(f"AltSpam Four Started !")    

    if config.SESSION5:
        await five.start()
        get_me5 = await five.get_me()
        alt5 = get_me5.id
        config.SUDO_USERS.append(alt5)
        try:
            await five.join_chat("TeamSirion")
            await five.join_chat("TheAltron")
            await five.join_chat("AltronChats")
            await five.join_chat("AltSpam")
        except:
            pass
        LOGGER("AltSpam").info(f"AltSpam Five Started !")

