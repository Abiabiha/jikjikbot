from rubpy import Client
from config import PHONE_NUMBER

bot = Client(phone_number=PHONE_NUMBER)

@bot.on_message()
async def handler(event):
    # پاسخ به کلمه سلام
    if event.message.text == "سلام":
        await event.reply("سلام! ربات فعال است.")

print("Bot is running...")
bot.run()
