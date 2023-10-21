# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License.
#

""" Userbot module for System Stats commands """

import asyncio
import platform
import sys
import time
from asyncio import create_subprocess_exec as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE
from datetime import datetime
from os import remove
from platform import python_version
from shutil import which

import psutil
from telethon import __version__, version

from AyiinXd import CMD_HELP, StartTime
from AyiinXd.ayiin import (
    HOSTED_ON,
    bash,
    edit_or_reply,
    ayiin_cmd,
)

from . import cmd, var
from .ping import get_readable_time

try:
    from carbonnow import Carbon
except ImportError:
    Carbon = None

modules = CMD_HELP
emoji = var.ALIVE_EMOJI
alive_text = var.ALIVE_TEKS_CUSTOM


@ayiin_cmd(
    pattern="sysinfo$",
)
async def _(e):
    xxnx = await edit_or_reply(e, "`Processing...`")
    x, y = await bash("neofetch|sed 's/\x1B\\[[0-9;\\?]*[a-zA-Z]//g' >> neo.txt")
    with open("neo.txt", "r") as neo:
        p = (neo.read()).replace("\n\n", "")
    ok = Carbon(base_url="https://carbonara.vercel.app/api/cook", code=p)
    haa = await ok.memorize("neofetch")
    await e.reply(file=haa)
    await xxnx.delete()
    remove("neo.txt")


@ayiin_cmd(pattern=r"spc")
async def psu(event):
    uname = platform.uname()
    softw = "**ɪɴғᴏʀᴍᴀsɪ sɪsᴛᴇᴍ**\n"
    softw += f"**sɪsᴛᴇᴍ   :** `{uname.system}`\n"
    softw += f"**ʀɪʟɪs    :** `{uname.release}`\n"
    softw += f"**ᴠᴇʀsɪ    :** `{uname.version}`\n"
    softw += f"**ᴍᴇsɪɴ    :** `{uname.machine}`\n"
    # Boot Time
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    softw += f"**ᴡᴀᴋᴛᴜ ʜɪᴅᴜᴘ:** `{bt.day}/{bt.month}/{bt.year}  {bt.hour}:{bt.minute}:{bt.second}`\n"
    # CPU Cores
    cpuu = "**ɪɴғᴏʀᴍᴀsɪ CPU**\n"
    cpuu += "**ᴘʜʏsɪᴄᴀʟ ᴄᴏʀᴇs   :** `" + \
        str(psutil.cpu_count(logical=False)) + "`\n"
    cpuu += "**ᴛᴏᴛᴀʟ ᴄᴏʀᴇs      :** `" + \
        str(psutil.cpu_count(logical=True)) + "`\n"
    # CPU frequencies
    cpufreq = psutil.cpu_freq()
    cpuu += f"**ᴍᴀx ғʀᴇᴏ̨ᴜᴇɴᴄʏ    :** `{cpufreq.max:.2f}Mhz`\n"
    cpuu += f"**ᴍɪɴ ғʀᴇᴏ̨ᴜᴇɴᴄʏ    :** `{cpufreq.min:.2f}Mhz`\n"
    cpuu += f"**ᴄᴜʀʀᴇɴᴛ ғʀᴇᴏ̨ᴜᴇɴᴄʏ:** `{cpufreq.current:.2f}Mhz`\n\n"
    # CPU usage
    cpuu += "**CPU ᴜsᴀɢᴇ ᴘᴇʀ ᴄᴏʀᴇ**\n"
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
        cpuu += f"**ᴄᴏʀᴇ {i}  :** `{percentage}%`\n"
    cpuu += "**ᴛᴏᴛᴀʟ CPU ᴜsᴀɢᴇ**\n"
    cpuu += f"**sᴇᴍᴜᴀ ᴄᴏʀᴇ:** `{psutil.cpu_percent()}%`\n"
    # RAM Usage
    svmem = psutil.virtual_memory()
    memm = "**ᴍᴇᴍᴏʀʏ ᴅɪɢᴜɴᴀᴋᴀɴ**\n"
    memm += f"**ᴛᴏᴛᴀʟ     :** `{get_size(svmem.total)}`\n"
    memm += f"**ᴀᴠᴀɪʟᴀʙʟᴇ :** `{get_size(svmem.available)}`\n"
    memm += f"**ᴜsᴇᴅ      :** `{get_size(svmem.used)}`\n"
    memm += f"**ᴘᴇʀᴄᴇɴᴛᴀɢᴇ :** `{svmem.percent}%`\n"
    # Bandwidth Usage
    bw = "**ʙᴀɴᴅᴡɪᴛʜ ᴅɪɢᴜɴᴀᴋᴀɴ**\n"
    bw += f"**ᴜɴɢɢᴀʜ  :** `{get_size(psutil.net_io_counters().bytes_sent)}`\n"
    bw += f"**ᴅᴏᴡɴʟᴏᴀᴅ :** `{get_size(psutil.net_io_counters().bytes_recv)}`\n"
    help_string = f"{softw}\n"
    help_string += f"{cpuu}\n"
    help_string += f"{memm}\n"
    help_string += f"{bw}\n"
    help_string += "**ɪɴғᴏʀᴍᴀsɪ ᴍᴇsɪɴ**\n"
    help_string += f"**ᴘʏᴛʜᴏɴ :** `{sys.version}`\n"
    help_string += f"**ᴛᴇʟᴇᴛʜᴏɴ :**`{__version__}`\n"
    help_string += f"**ᴘʏ-ᴇʙᴏᴡ :** `0.4.6`\n"
    help_string += f"**ᴇʙᴏᴡ-ᴠᴇʀsɪᴏɴ :** `{var.BOT_VER} [{HOSTED_ON}]`"
    await edit_or_reply(event, help_string)


def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


@ayiin_cmd(pattern="sysd$")
async def sysdetails(sysd):
    if not sysd.text[0].isalpha() and sysd.text[0] not in ("/", "#", "@", "!"):
        try:
            fetch = await asyncrunapp(
                "neofetch",
                "--stdout",
                stdout=asyncPIPE,
                stderr=asyncPIPE,
            )

            stdout, stderr = await fetch.communicate()
            result = str(stdout.decode().strip()) + \
                str(stderr.decode().strip())

            await edit_or_reply(sysd, "`" + result + "`")
        except FileNotFoundError:
            await edit_or_reply(sysd, "**Install neofetch Terlebih dahulu!!**")


@ayiin_cmd(pattern="botver$")
async def bot_ver(event):
    if event.text[0].isalpha() or event.text[0] in ("/", "#", "@", "!"):
        return
    if which("git") is not None:
        ver = await asyncrunapp(
            "git",
            "describe",
            "--all",
            "--long",
            stdout=asyncPIPE,
            stderr=asyncPIPE,
        )
        stdout, stderr = await ver.communicate()
        verout = str(stdout.decode().strip()) + str(stderr.decode().strip())

        rev = await asyncrunapp(
            "git",
            "rev-list",
            "--all",
            "--count",
            stdout=asyncPIPE,
            stderr=asyncPIPE,
        )
        stdout, stderr = await rev.communicate()
        revout = str(stdout.decode().strip()) + str(stderr.decode().strip())

        await edit_or_reply(
            event,
            "• **Userbot Versi :** " f"`{verout}`" "\n• **Revisi :** " f"`{revout}`",
        )
    else:
        await edit_or_reply(
            event, "anda tidak memiliki git, Anda Menjalankan Bot - 'v1.beta.4'!"
        )


@ayiin_cmd(pattern="(?:alive|yinson)\\s?(.)?")
async def amireallyalive(alive):
    user = await alive.client.get_me()
    uptime = await get_readable_time((time.time() - StartTime))
    await alive.edit("😈")
    await asyncio.sleep(3)
    output = (
        f"❏ 𝗧𝗛𝗘 **[𝗘𝗕𝗢𝗪-𝗨𝗦𝗘𝗥𝗕𝗢𝗧](https://github.com/c0dsx/Ebow-Userbot) 𝗣𝗥𝗘𝗦𝗘𝗡𝗧**\n\n"
        f"**ʜᴇʏ, sᴀʏᴀ ᴘᴇɴɢɢᴜɴᴀ ᴇʙᴏᴡ-ᴜsᴇʀʙᴏᴛ**\n\n"
        f"• **ᴇʙᴏᴡ ᴠᴇʀsɪᴏɴ :** `{var.BOT_VER}`\n"
        f"• **ʙᴏᴛ ᴜᴘᴛɪᴍᴇ :** `{uptime}`\n"
        f"• **ᴅᴇᴘʟᴏʏ ᴏɴ :** {HOSTED_ON}\n"
        f"• **ᴍᴏᴅᴜʟᴇs :** `{len(modules)} Modules` \n"
        f"• **ᴏᴡɴᴇʀ :** [{user.first_name}](tg://user?id={user.id}) \n"
        f"• **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{python_version()}` \n"
        f"• **ᴘʏᴛɢᴄᴀʟʟs ᴠᴇʀsɪᴏɴ :** `Unlimited` \n"
        f"• **ᴘʏ-ᴇʙᴏᴡ ᴠᴇʀsɪᴏɴ :** `0.4.6`\n"
        f"• **ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀsɪᴏɴ :** `{version.__version__}` \n\n"
    )
    if var.ALIVE_LOGO:
        try:
            logo = var.ALIVE_LOGO
            await alive.delete()
            await alive.client.send_file(alive.chat_id, logo, caption=output)
        except BaseException:
            await alive.edit(
                output
            )
            return
    else:
        await edit_or_reply(alive, output)


CMD_HELP.update(
    {
        "system": f"**Plugin : **`system`.\
        \n\n  »  **Perintah :** `{cmd}sysinfo`\
        \n  »  **Kegunaan : **Informasi sistem menggunakan neofetch mengirim sebagai gambar.\
        \n\n  »  **Perintah :** `{cmd}sysd`\
        \n  »  **Kegunaan : **Informasi sistem menggunakan neofetch.\
        \n\n\n  »  **Perintah :** `{cmd}botver`\
        \n  »  **Kegunaan : **Menampilkan versi userbot.\
        \n\n  »  **Perintah :** `{cmd}spc`\
        \n  »  **Kegunaan : **Menampilkan spesifikasi sistem secara lengkap.\
    "
    }
)


CMD_HELP.update(
    {
        "alive": f"**Plugin : **`alive`\
        \n\n  »  **Perintah :** `{cmd}alive` atau `{cmd}yinson`\
        \n  »  **Kegunaan : **Untuk melihat apakah bot Anda berfungsi atau tidak.\
    "
    }
)
