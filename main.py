import os
from pyrogram import Client, filters
import logging

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.INFO
)


API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")


app = Client(name="rawupdate", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


@app.on_message(filters.command("start"))
async def start_handler(client, message):
    logging.info("start_handler executed")
    await client.send_message(
        chat_id=message.from_user.id,
        text=f"**Hello {message.from_user.first_name},\nI am a Telegram RAW Update Bot\n\n✅ Developed By: @PrimeAkash**",
    )
    logging.info(f"{message.from_user.first_name} started the bot")


@app.on_message()
async def raw_handler(client, message):
    logging.info("raw update handler executed")
    await client.send_message(
        chat_id=message.from_user.id,
        text=f"**📂Telegram RAW Update**\n\n```{message}```\n\n**✅Developed By: @PrimeAkash**",
    )
    logging.info(f"{message.from_user.first_name} got the raw update")


app.run()
