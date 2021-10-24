from aiogram import types
from misc import dp,bot
import sqlite3
from .sqlit import reg_user

@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    reg_user(message.chat.id,'123')

    markup = types.InlineKeyboardMarkup()
    bat_a = types.InlineKeyboardButton(text='✅ОТКРЫТЬ ДОСТУП', callback_data= f'start_watch_')
    markup.add(bat_a)
    await bot.send_video(video='BAACAgIAAxkBAAMHYXVAxIg5nV_8KGaG9U5LuGlIn1MAApkPAALbzrFLzAqE_GWqJlQhBA', caption="""<b>🔞Фулл уже загружен в нашего бота</b>

📲Приятного просмотра 👇👇👇""",parse_mode='html',reply_markup=markup,chat_id=message.chat.id)

