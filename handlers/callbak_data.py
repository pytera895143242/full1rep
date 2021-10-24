from aiogram import types
from misc import dp, bot
from .sqlit import cheak_traf,reg_user,cheak_chat_id

reg_user(1,1)

full_video = 'BAACAgIAAxkBAAMfYXVDQXU8i_9_M_hM2mCrQaxHptcAApEPAALbzrFLI-w6_KUKGkUhBA'

list_channel = cheak_traf()
name_channel_1 = list_channel[0]
name_channel_2 = list_channel[1]
name_channel_3 = list_channel[2]
name_channel_4 = list_channel[3]

def obnovlenie():
    global name_channel_1,name_channel_2,name_channel_3,name_channel_4
    list_channel = cheak_traf()
    name_channel_1 = list_channel[0]
    name_channel_2 = list_channel[1]
    name_channel_3 = list_channel[2]
    name_channel_4 = list_channel[3]


@dp.callback_query_handler(text_startswith='start_watch')  # Нажал кнопку Начать смотреть
async def start_watch(call: types.callback_query):

    markup = types.InlineKeyboardMarkup()
    bat_a = types.InlineKeyboardButton(text='Я ПОДПИСАЛСЯ🍑', callback_data=f'check')
    markup.add(bat_a)

    await bot.send_message(call.message.chat.id, f"""<b>⚠️ ДОСТУП ЗАКРЫТ</b>

⚙️Для просмотра фулла необходимо подписаться на ниже указанные каналы

📍После этого жми кнопку «Я ПОДПИСАЛСЯ🍑»

<b>Канал 1</b> - {name_channel_1}
<b>Канал 2</b> - {name_channel_2}
<b>Канал 3</b> - {name_channel_3}
<b>Канал 4</b> - {name_channel_4}""", parse_mode='html',reply_markup=markup,disable_web_page_preview=True)




@dp.callback_query_handler(text_startswith='check')  # Нажал кнопку Я ПОДПИСАЛСЯ. ДЕЛАЕМ ПРОВЕРКУ
async def check(call: types.callback_query):
    await bot.send_message(call.message.chat.id, '⏳ Ожидайте. Идёт проверка подписки.')
    name_channel = call.data[5:]
    id_list = cheak_chat_id()

    try:
        proverka1 = (await bot.get_chat_member(chat_id=id_list[0], user_id=call.message.chat.id)).status
    except:
        proverka1 = 'member'

    try:
        proverka2 = (await bot.get_chat_member(chat_id=id_list[1], user_id=call.message.chat.id)).status
    except:
        proverka2 = 'member'

    try:
        proverka3 = (await bot.get_chat_member(chat_id=id_list[2], user_id=call.message.chat.id)).status
    except:
        proverka3 = 'member'

    try:
        proverka4 = (await bot.get_chat_member(chat_id=id_list[3], user_id=call.message.chat.id)).status
    except:
        proverka4 = 'member'

    markup = types.InlineKeyboardMarkup()
    bat_a = types.InlineKeyboardButton(text='Я ПОДПИСАЛСЯ🍑', callback_data=f'check{name_channel}')
    markup.add(bat_a)

    if (proverka1 == 'member' and proverka2 == 'member' and proverka3 == 'member' and proverka4 == 'member') or proverka1 == 'administrator' or proverka2 == 'administrator' or proverka3 == 'administrator' or proverka1 == 'creator' or proverka2 == 'creator' or proverka3 == 'creator' or proverka4 == 'administrator' or proverka4 == 'creator': #Человек прошел все 2 проверки
        markup_2 = types.InlineKeyboardMarkup()
        list = cheak_traf()  #ПОЛУЧАЕТ ЛИСТ
        bat1 = types.InlineKeyboardButton(text='Гоу еще🔥',callback_data='content_two')
        markup_2.add(bat1)
        await bot.send_video(chat_id=call.message.chat.id,video='BAACAgIAAxkBAAMkYXVGlJvN7O0li3zerx0TzPC6IKUAApEPAALbzrFLI-w6_KUKGkUhBA',caption="""👆А ВОТ И ФУЛЛ

🔝Если хочешь еще больше топового контента, жми кнопку <b>«Гоу еще🔥»</b>""",reply_markup=markup_2,parse_mode='html')


    else:
        await bot.send_message(call.message.chat.id, '❌Вы не подписались на каналы ниже\n\n'
                                                     'Проверьте подписку на все каналы. И затем жми кнопку <b>Я ПОДПИСАЛСЯ🍑</b> для проверки!\n\n'
                                                     f'<b>Канал 1</b> - {name_channel_1}\n'
                                                     f'<b>Канал 2</b> - {name_channel_2}\n'
                                                     f'<b>Канал 3</b> - {name_channel_3}\n'
                                                     f'<b>Канал 4</b> - {name_channel_4}',parse_mode='html',reply_markup=markup,disable_web_page_preview=True)