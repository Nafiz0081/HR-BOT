import os
import asyncio
from telegram.ext import ApplicationBuilder

async def main():
    print("Bot is starting...")

    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    if not token:
        raise ValueError("TELEGRAM_BOT_TOKEN not set!")

    app = ApplicationBuilder().token(token).build()
    
    async with app:
        print("Bot is running!")
        await app.start()
        await app.updater.start_polling()
        
        # Keep running forever
        await asyncio.sleep(float("inf"))

if __name__ == "__main__":
    asyncio.run(main())