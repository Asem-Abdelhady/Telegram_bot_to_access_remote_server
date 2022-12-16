from pyrogram import Client, filters
from pyrogram.types import Message
from dotenv import load_dotenv
import os
import subprocess

# try github action v1

load_dotenv('.env')

app = Client("my_account", api_id=os.environ['API_ID'], api_hash=os.environ['API_HASH'],
             bot_token=os.environ['BOT_TOKEN'])


async def check_owner(tg_id):
    if not tg_id == int(os.environ['TG_ID']):
        await app.send_message(tg_id, "Not your PC!!")
        return False
    return True


@app.on_message(filters.command('ls') & filters.private)
async def ls(client: Client, message: Message):
    user_id = message.from_user.id
    if not await check_owner(user_id): return
    await app.send_message(user_id, "\n".join(os.listdir(os.getcwd())))


@app.on_message(filters.command('cd') & filters.private)
async def cd(client: Client, message: Message):
    user_id = message.from_user.id
    if not await check_owner(user_id): return
    os.chdir(message.command[1])
    await app.send_message(user_id, f'Current directory {os.getcwd()}')


@app.on_message(filters.command('get') & filters.private)
async def get(client: Client, message: Message):
    user_id = message.from_user.id
    if not await check_owner(user_id): return
    await app.send_document(user_id, f'{os.getcwd()}{os.path.sep}{message.command[1]}')


@app.on_message(filters.command('run') & filters.private)
async def run(client: Client, message: Message):
    user_id = message.from_user.id
    if not await check_owner(user_id): return
    result = subprocess.run(message.command[1:], capture_output=True, text=True)
    await app.send_message(user_id, result.stdout)


app.run()
