import asyncio
import json
from rubika_bot_api.api import Robot

TOKEN = "BHIDFC0YJPMRIWXBIHCWQKCHLXRQTKLKPLOISTWWDJTRBXALRLOGWWPPXSRQSAFQ"

bot = Robot(token=TOKEN)

@bot.on_message()
async def debug(bot_instance, message):
    print("=" * 50)
    print(json.dumps(message.raw_data, indent=2, ensure_ascii=False))

    if message.chat_id:
        await message.reply("✅ پیام دریافت شد")

if __name__ == "__main__":
    asyncio.run(bot.run())
