import asyncio

from aiogram import types
from misc import dp, bot
from .sqlit import cheak_traf,reg_user,cheak_chat_id

start2_photo = 'AgACAgIAAxkBAAM6YXVJZ_qZedAObKAHwiUiGQjMB5MAAk21MRsSdalL89Mq2-czTYwBAAMCAAN5AAMhBA'

chat1 = -1001705301667
chat2 = -1001567462615
chat3 = -1001478210539

@dp.callback_query_handler(text_startswith='content_two')  # Нажал кнопку Хочу еще
async def start_watch(call: types.callback_query):

    markup = types.InlineKeyboardMarkup()
    bat_a = types.InlineKeyboardButton(text='✅ОТКРЫТЬ ДОСТУП', callback_data=f'two_check')
    markup.add(bat_a)
    await bot.send_photo(photo=start2_photo, caption="""<b>🔞БУХОЙ ОДНОКУРСНИК ВЫЕБАЛ ДАШУ В ПЕРВЫЙ РАЗ КОГДА ОСТАЛИСЬ ОДНИ ДОМА!
И ЗАПИСАЛ НА ТЕЛЕФОН 📲</b>

⚙️Для просмотра фулла необходимо подписаться на ниже указанные каналы

📍После этого жми кнопку <b>«✅ОТКРЫТЬ ДОСТУП»</b>

<b>Канал 1</b> - https://t.me/joinchat/TacJRh9e8j1kNWJi
<b>Канал 2</b> - https://t.me/joinchat/GDaPlcPaF2VlMDYy
<b>Канал 3</b> - https://t.me/joinchat/iv8WoTLuO5UwYWUy""", parse_mode='html', reply_markup=markup, chat_id=call.message.chat.id)


@dp.callback_query_handler(text='two_check')  # Нажал кнопку Я ПОДПИСАЛСЯ. ДЕЛАЕМ ПРОВЕРКУ
async def check2(call: types.callback_query):

    await bot.send_message(call.message.chat.id, '⏳ Ожидайте. Идёт проверка подписки.')

    try:
        proverka1 = (await bot.get_chat_member(chat_id=chat1, user_id=call.message.chat.id)).status
    except:
        proverka1 = 'member'

    try:
        proverka2 = (await bot.get_chat_member(chat_id=chat1, user_id=call.message.chat.id)).status
    except:
        proverka2 = 'member'

    try:
        proverka3 = (await bot.get_chat_member(chat_id=chat3, user_id=call.message.chat.id)).status
    except:
        proverka3 = 'member'


    markup = types.InlineKeyboardMarkup()
    bat_a = types.InlineKeyboardButton(text='Я ПОДПИСАЛСЯ🍑', callback_data='two_check')
    markup.add(bat_a)

    markup_finish = types.InlineKeyboardMarkup()

    list_channel = cheak_traf()
    name_channel_1 = list_channel[0]

    bat_a = types.InlineKeyboardButton(text='ГОДНОТА 18+', url='https://t.me/joinchat/5BysUlaORp5kMjhi')
    markup_finish.add(bat_a)

    if (proverka1 == 'member' and proverka2 == 'member' and proverka3 == 'member') or proverka1 == 'administrator' or proverka2 == 'administrator' or proverka3 == 'administrator' or proverka1 == 'creator' or proverka2 == 'creator' or proverka3 == 'creator': #Человек прошел все 2 проверки
        await bot.send_video(chat_id=call.message.chat.id,video='BAACAgIAAxkBAAM-YXVOHFBB-d0PqGl_fDS7FP6pZrEAAkAIAAIqdthKgxJR-2SAuG8hBA',caption="""<b>👆А ВОТ И ФУЛЛ</b>
        
Еще больше топового контента в нашем канале👇
""",parse_mode='html',reply_markup=markup_finish)



    else:
        await bot.send_message(call.message.chat.id, '❌Вы не подписались на каналы ниже\n\n'
                                                     'Проверьте подписку на все каналы. И затем жми кнопку <b>Я ПОДПИСАЛСЯ🍑</b> для проверки!\n\n'
                                                     f'<b>Канал 1</b> - https://t.me/joinchat/TacJRh9e8j1kNWJi\n'
                                                     f'<b>Канал 2</b> - https://t.me/joinchat/GDaPlcPaF2VlMDYy\n'
                                                     f'<b>Канал 3</b> - https://t.me/joinchat/iv8WoTLuO5UwYWUy\n',parse_mode='html',reply_markup=markup,disable_web_page_preview=True)