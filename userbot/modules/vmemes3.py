

from time import sleep
from userbot import CMD_HELP, bot
from userbot.events import register
from telethon import events
import asyncio


@register(outgoing=True, pattern="^.hua$")
async def koc(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        await e.edit("Aku di ghosting")
        sleep(1)
        await e.edit("ð­ð­ð­")
        sleep(1)
        await e.edit("Aku Sedihhh")
        sleep(1)
        await e.edit("Kenapa si")
        sleep(1)
        await e.edit("GAMPANG BGT NYAKITIN")
        sleep(1)
        await e.edit("HATI GUA BUKAN BUAT DI GHOSTING")
        sleep(1)
        await e.edit("TAI BANGET ASLI")
        sleep(1)
        await e.edit("PARAH SI")
        sleep(1)
        await e.edit("DEMI APASII")
        sleep(1)
        await e.edit("TWINGG")
        sleep(1)
        await e.edit("KONTOL")
        sleep(1)
        await e.edit("MEMEK")
        sleep(1)
        await e.edit("AKU DI GHOSTING")
        sleep(1)
        await e.edit("BANGSAT")
        sleep(1)
        await e.edit("ANJING")
        sleep(1)
        await e.edit("ð¡ð¡ð¡")
        sleep(1)
        await e.edit("ð¥´ð¥´ð¥´")
        sleep(1)
        await e.edit("ANJINGGGGà¼¼")
        sleep(1)
        await e.edit("TAIIII")
        sleep(1)
        await e.edit("AH ELAHH BABI")
        sleep(1)
        await e.edit("GAUSAH GANGGU")
        sleep(1)
        await e.edit("GUA STRESS")
        sleep(1)
        await e.edit("ð­ð­ð­ð­ð­ð­")
        sleep(1)
        await e.edit("ð¥´ð¥´ð¥´ð¥´")
        sleep(1)
        await e.edit("ADA YG MAU SAMA GUA?")
        sleep(1)
        await e.edit("PLISS GUA BUTUH")
        sleep(1)
        await e.edit("SESEORANG YG MAU NERIMA GUA")
        sleep(1)
        await e.edit("ðððð")
        sleep(1)
        await e.edit("MAU GAK JADI PACAR GUA??à¼¼")
        sleep(1)
        await e.edit("à¼¼ TAPI BOONG TOD!!à¼½")


@register(outgoing=True, pattern='^.huh(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n(\\_/)`"
                     "`\n(â_â)`"
                     "`\n />â¤ï¸ *NIH GUA KASIH BUAT LU!!`")
    sleep(3)
    await typew.edit("`\n(\\_/)`"
                     "`\n(â_â)`"
                     "`\n/>ð  *E GAK DEH,UDH DI KSH GRATIS LU RUSAKIN`")
    sleep(2)
    await typew.edit("`\n(\\_/)`"
                     "`\n(â_â)`"
                     "`\nð<\\  *KENTOD`")


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 3

    animation_ttl = range(0, 103)

    input_str = event.pattern_match.group(1)

    if input_str == "story":

        await event.edit(input_str)

        animation_chars = [
            "`Cerita â¤ï¸ Cinta` ",
            "  ð             ð \n/ð\\         <ð\\ \n ð               /|",
            "  ð          ð³ \n/ð\\       /ð\\ \n  ð            /|",
            "  ð            ð \n/ð\\         <ð> \n  ð             /|",
            "  ð         âºï¸ \n/ð\\      /ð\\ \n  ð          /|",
            "  ð          ð \n/ð\\       /ð\\ \n  ð           /|",
            "  ð   ð \n /ð\\/ð\\ \n   ð   /|",
            " ð³  ð \n /|\\ /ð\\ \n /     / |",
            "ð    /ð°\\ \n<|\\      ð \n /ð    / |",
            "ð \n/(),âð® \n /\\         _/\\/|",
            "ð \n/\\_,__ð« \n  //    //       \\",
            "ð \n/\\_,ð¦_ð  \n  //         //        \\",
            "  ð­      âºï¸ \n  /|\\   /(ð¶)\\ \n  /!\\   / \\ ",
            "`TAMAT ð`"]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 103])


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 11)

    input_str = event.pattern_match.group(1)

    if input_str == "canda":

        await event.edit(input_str)

        animation_chars = [
            "`â â â â£ â£¶â¡¾â â â â ³â¢¦â¡â â â â¢ â â â â ²â¡â \n â â£´â ¿â â â â â â    â¢³â¡â â¡â â â    â â¢·\nâ¢ â£â£â¡â¢â£â£â¡â â£â¡â£§â â¢¸â â â   â    â¡\nâ¢¸â£¯â¡­â â ¸â£â£â â¡´â£»â¡²â£¿  â£¸ Kamu    â¡\n â£â£¿â¡­â â â â â â¢±â â   â£¿  â¢¹â         â¡\n  â â¢¿â£¯â â â â __â â â¡¿ â â¡â â â â     â¡¼\nâ â â â ¹â£¶â â â â â â â¡´â â    â â ¤â£â£ â â \nâ â â â â¢¸â£·â¡¦â¢¤â¡¤â¢¤â£â£â â â â â â â â â â \nâ â¢â£¤â£´â£¿â£â â â â ¸â£â¢¯â£·â£â£¦â¡â â â â â â \nâ¢â£¾â£½â£¿â£¿â£¿â£¿â â¢²â£¶â£¾â¢â¡·â£¿â£¿â µâ£¿â â â â â â \nâ£¼â£¿â â â£¿â¡­â â â¢ºâ£â£¼â¡â â  â â£â¢¸â â â â â â `",
            "`â â â â£ â£¶â¡¾â â â â ³â¢¦â¡â â â â¢ â â â â ²â¡â \n â â£´â ¿â â â â â â   â â¢³â¡â â¡â â â    â â¢·\nâ¢ â£â£â¡â¢â£â£â¡â â£â¡â£§â â¢¸â â â       â¡\nâ¢¸â£¯â¡­â â ¸â£â£â â¡´â£»â¡²â£¿  â£¸ Pasti   â¡\n â£â£¿â¡­â â â â â â¢±â â   â£¿  â¢¹â         â¡\n  â â¢¿â£¯â â â |__|â â â¡¿ â â¡â â â â     â¡¼\nâ â â â ¹â£¶â â â â â â â¡´â â    â â ¤â£â£ â â \nâ â â â â¢¸â£·â¡¦â¢¤â¡¤â¢¤â£â£â â â â â â â â â â \nâ â¢â£¤â£´â£¿â£â â â â ¸â£â¢¯â£·â£â£¦â¡â â â â â â \nâ¢â£¾â£½â£¿â£¿â£¿â£¿â â¢²â£¶â£¾â¢â¡·â£¿â£¿â µâ£¿â â â â â â \nâ£¼â£¿â â â£¿â¡­â â â¢ºâ£â£¼â¡â â  â â£â¢¸â â â â â â `",
            "`â â â â£ â£¶â¡¾â â â â ³â¢¦â¡â â â â¢ â â â â ²â¡â \n â â£´â ¿â â â      â â¢³â¡â â¡â â     â â¢·\nâ¢ â£â£â¡â¢â£â£â¡â â£â¡â£§â â¢¸â â â â      â¡\nâ¢¸â£¯â¡­â â ¸â£â£â â¡´â£»â¡²â£¿  â£¸ Belum   â¡\n â£â£¿â¡­â â â â â â¢±â â   â£¿  â¢¹â          â¡\n  â â¢¿â£¯â â â (x)â â â¡¿ â â¡â â â â     â¡¼\nâ â â â ¹â£¶â â â â â â â¡´â â    â â ¤â£â£ â â \nâ â â â â¢¸â£·â¡¦â¢¤â¡¤â¢¤â£â£â â â â â â â â â â \nâ â¢â£¤â£´â£¿â£â â â â ¸â£â¢¯â£·â£â£¦â¡â â â â â â \nâ¢â£¾â£½â£¿â£¿â£¿â£¿â â¢²â£¶â£¾â¢â¡·â£¿â£¿â µâ£¿â â â â â â \nâ£¼â£¿â â â£¿â¡­â â â¢ºâ£â£¼â¡â â  â â£â¢¸â â â â â â `",
            "`â â â â£ â£¶â¡¾â â â â ³â¢¦â¡â â â â¢ â â â â ²â¡â \n â â£´â ¿â â â      â â¢³â¡â â¡â â     â â¢·\nâ¢ â£â£â¡â¢â£â£â¡â â£â¡â£§â â¢¸â    â      â¡\nâ¢¸â£¯â¡­â â ¸â£â£â â¡´â£»â¡²â£¿  â£¸ Mandi Wajib  â¡\n â£â£¿â¡­â â â â â â¢±â    â£¿  â¢¹â         â¡\n  â â¢¿â£¯â â â â __ â â â¡¿ â â¡â â â â     â¡¼\nâ â â â ¹â£¶â â â â â â â¡´â â    â â ¤â£â£ â â \nâ â â â â¢¸â£·â¡¦â¢¤â¡¤â¢¤â£â£â â â â â â â â â â \nâ â¢â£¤â£´â£¿â£â â â â ¸â£â¢¯â£·â£â£¦â¡â â â â â â \nâ¢â£¾â£½â£¿â£¿â£¿â£¿â â¢²â£¶â£¾â¢â¡·â£¿â£¿â µâ£¿â â â â â â \nâ£¼â£¿â â â£¿â¡­â â â¢ºâ£â£¼â¡â â  â â£â¢¸â â â â â â `",
            "`â â â â£ â£¶â¡¾â â â â ³â¢¦â¡â â â â¢ â â â â ²â¡â \n â â£´â ¿â â â â â â    â¢³â¡â â¡â â     â â¢·\nâ¢ â£â£â¡â¢â£â£â¡â â£â¡â£§â â¢¸â â  â      â¡\nâ¢¸â£¯â¡­â â ¸â£â£â â¡´â£»â¡²â£¿  â£¸ Bwhaha  â¡\n â£â£¿â¡­â â â â â â¢±â â   â£¿  â¢¹â         â¡\n  â â¢¿â£¯â â â |__| â â¡¿ â â¡â â â â     â¡¼\nâ â â â ¹â£¶â â â â â â â¡´â â    â â ¤â£â£ â â \nâ â â â â¢¸â£·â¡¦â¢¤â¡¤â¢¤â£â£â â â â â â â â â â \nâ â¢â£¤â£´â£¿â£â â â â ¸â£â¢¯â£·â£â£¦â¡â â â â â â \nâ¢â£¾â£½â£¿â£¿â£¿â£¿â â¢²â£¶â£¾â¢â¡·â£¿â£¿â µâ£¿â â â â â â \nâ£¼â£¿â â â£¿â¡­â â â¢ºâ£â£¼â¡â â  â â£â¢¸â â â â â â `",
            "`â â â â£ â£¶â¡¾â â â â ³â¢¦â¡â â â â¢ â â â â ²â¡â \n â â£´â ¿â â â â â â   â â¢³â¡â â¡â â     â â¢·\nâ¢ â£â£â¡â¢â£â£â¡â â£â¡â£§â â¢¸â   â      â¡\nâ¢¸â£¯â¡­â â ¸â£â£â â¡´â£»â¡²â£¿  â£¸ GOBLOK   â¡\n â£â£¿â¡­â â â â â â¢±â    â£¿  â¢¹â         â¡\n  â â¢¿â£¯â â â ****â â â¡¿ â â¡â â â â     â¡¼\nâ â â â ¹â£¶â â â â â â â¡´â â    â â ¤â£â£ â â \nâ â â â â¢¸â£·â¡¦â¢¤â¡¤â¢¤â£â£â â â â â â â â â â \nâ â¢â£¤â£´â£¿â£â â â â ¸â£â¢¯â£·â£â£¦â¡â â â â â â \nâ¢â£¾â£½â£¿â£¿â£¿â£¿â â¢²â£¶â£¾â¢â¡·â£¿â£¿â µâ£¿â â â â â â \nâ£¼â£¿â â â£¿â¡­â â â¢ºâ£â£¼â¡â â  â â£â¢¸â â â â â â `"]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 11])


@register(outgoing=True, pattern='^.nah(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`\n(\\_/)`"
                     "`\n(â_â)`"
                     "`\n />ð *Ini Buat Kamu`")
    sleep(2)
    await typew.edit("`\n(\\_/)`"
                     "`\n(â_â)`"
                     "`\nð<\\  *Tapi Bo'ong`")
# Alpinnnn Gans


@bot.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 6)

    input_str = event.pattern_match.group(1)

    if input_str == "owner":

        await event.edit(input_str)

        animation_chars = [
            "**OWNER BAGAS-UBOT ADALAH TUHAN DARI SEKTE BAGASNISM , YUK SABI YUK MASUK SEKTE BAGAS.., **"
            "**OKE BIARKAN SAYA INTRO DULU.. **"
            "**GUA ATHEIS TAPI GUA PUNYA TUHAN.. **"
            "**SOLOYOLO WHAZZUP MY FRIENDS SOBAT SEKON GUA.. **"
            "**FAKKLAHH.. **"
            "**NGENSKUYYY.. **"
            "**ANJASSS BROOOHH.. **"
            "**KENALIN GUA BAGAS.. **"
            "**BACOTNYA KADANG NGE GASS..!!**"
            "**TAPI JANGAN BAPER..!!**"
            "**GUA IMIGRAN DARI SURGA, YANG DI TURUNKAN KE BUMI DI MALAM PENGANTIN DAN TEGANG.., **"
            "**UMUR GUA DUAPULUH DI TAMBAH TIGA, DI KURANGIN 1.., **"
            "**GUA ANAK KE DUA DARI TIGA BERSAUDARA..**"
            "**ASKOT GUA JATENG PAS NYA DI SOLO..**"
            "**KALO MAU MAIN SINI PC AJA , TAPI BAWAIN ROKOK SAMA KOPI, JANGAN NYUSAHIN, NGENTOTT..!!**"]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 6])

CMD_HELP.update({
    "memes5":
    "`.nah` ; `.huh` ; `.owner`\
    \nUsage: cobain.\
    \n\n`.bunga` ; `.buah`\
    \nUsage: animasi.\
    \n\n`.waktu`\
    \nUsage: animasi."
})

CMD_HELP.update({
    "memes6":
    "`.hua`\
    \nUsage: nangis.\
    \n\n`.cinta` ; `.canda`\
    \nUsage: liat sendiri"
})
