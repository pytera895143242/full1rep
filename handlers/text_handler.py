from aiogram import types
from misc import dp,bot
import asyncio

@dp.message_handler(content_types=['video','photo','text'])
async def all_other_messages(message: types.message):
    print('12')
    print(message)