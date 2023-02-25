#Copyright ©️ 2022 MAMBA HACKERS. All Rights Reserved
#You are free to use this code in any of your project, but you MUST include the following in your README.md (Copy & paste)
# ##Credits - [MediaToTelegraphLink bot by MAMBA HACKERS] (https://github.com/FantasticSukhi/MTLG)

from pyrogram import Client, filters
from pyrogram.types import Message
from telegraph import upload_file
import os

teletips=Client(
    "MediaToTelegraphLink",
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
    bot_token = os.environ["BOT_TOKEN"]
)

@teletips.on_message(filters.command('start') & filters.private)
async def start(client, message):
    text = f"""
नमस्कार {message.from_user.mention},
मैं यहां आपकी मीडिया फाइलों के लिए टेलीग्राफ लिंक जेनरेट करने के लिए हूं.

सीधे इस चैट पर एक मान्य मीडिया फ़ाइल भेजें।
मान्य फ़ाइल प्रकार 'जेपीईजी', 'जेपीजी', 'पीएनजी', 'एमपी4' और 'जीआईएफ' हैं।

**ग्रुप चैट** में लिंक जेनरेट करने के लिए, मुझे अपने सुपरग्रुप में जोड़ें और कमांड <code>/tl</code> को मान्य मीडिया फ़ाइल के जवाब के रूप में भेजें।
🏠 | [Home](https://t.me/MAMBACLASSES)
            """
    await teletips.send_message(message.chat.id, text, disable_web_page_preview=True)
    

@teletips.on_message(filters.media & filters.private)
async def get_link_private(client, message):
    try:
        text = await message.reply("प्रक्रिया चल रही है...")
        async def progress(current, total):
            await text.edit_text(f"📥 मीडिया डाउनलोड हो रहा है... {current * 100 / total:.1f}%")
        try:
            location = f"./media/private/"
            local_path = await message.download(location, progress=progress)
            await text.edit_text("📤 टेलीग्राफ पर अपलोड हो रहा है...")
            upload_path = upload_file(local_path) 
            await text.edit_text(f"**🌐 | टेलीग्राफ लिंक**:\n\n<code>https://telegra.ph{upload_path[0]}</code>")     
            os.remove(local_path) 
        except Exception as e:
            await text.edit_text(f"**❌ | फ़ाइल अपलोड विफल**\n\n<i>**कारण**: {e}</i>")
            os.remove(local_path) 
            return                 
    except Exception:
        pass        

@teletips.on_message(filters.command('tl'))
async def get_link_group(client, message):
    try:
        text = await message.reply("प्रक्रिया चल रही है...")
        async def progress(current, total):
            await text.edit_text(f"📥 मीडिया डाउनलोड हो रहा है... {current * 100 / total:.1f}%")
        try:
            location = f"./media/group/"
            local_path = await message.reply_to_message.download(location, progress=progress)
            await text.edit_text("📤 टेलीग्राफ पर अपलोड हो रहा है....")
            upload_path = upload_file(local_path) 
            await text.edit_text(f"**🌐 | टेलीग्राफ लिंक**:\n\n<code>https://telegra.ph{upload_path[0]}</code>")     
            os.remove(local_path) 
        except Exception as e:
            await text.edit_text(f"**❌ | फ़ाइल अपलोड विफल**\n\n<i>**कारण**: {e}</i>")
            os.remove(local_path) 
            return         
    except Exception:
        pass                                           

print("Bot is alive!")
teletips.run()

#Copyright ©️ 2022 MAMBA HACKERS. All Rights Reserved
