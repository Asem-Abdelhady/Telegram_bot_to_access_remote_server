from pyrogram import Client, filters
from pyrogram.types import Message
from dotenv import load_dotenv
import os

load_dotenv('.env')

app = Client("my_account", api_id=os.environ['API_ID'], api_hash=os.environ['API_HASH'],
             bot_token=os.environ['BOT_TOKEN'])


@app.on_message(filters.command('ls') & filters.private)
async def ls(client: Client, message: Message):
    user_id = message.from_user.id
    await app.send_message(user_id, "\n".join(os.listdir(os.getcwd())))


@app.on_message(filters.command('cd') & filters.private)
async def cd(client: Client, message: Message):
    user_id = message.from_user.id
    os.chdir(message.command[1])
    await app.send_message(user_id, f'Current directory {os.getcwd()}')


@app.on_message(filters.command('get') & filters.private)
async def get(client: Client, message: Message):
    user_id = message.from_user.id
    await app.send_document(user_id, f'{os.getcwd()}{os.path.sep}{message.command[1]}')


app.run()
