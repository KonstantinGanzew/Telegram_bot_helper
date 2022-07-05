import config
import datetime
import erp
from aiogram import types, Dispatcher
from create_bot import bot
from googleDisk import google



# Отвечает на команду старт
async def command_start(message: types.Message):
    await log([message.from_user.id, message.from_user.first_name, message.from_user.username, message.text.replace('/it ', '')])
    if message.chat.id in config.CANNON_GROUP:
        await bot.send_message(message.chat.id, 'Бот для ведения задач. Для заведения задач необходимо написать /it и текст сообщения')
    if erp.authentications(message.from_user.id):
        await bot.send_message(message.from_user.id, 'Добро пожаловать на галеру фраерок...')


# Отправляет сообщение на гугл диск и создает процесс в ответ на команду /it
async def report_in_google_sheets(message: types.Message):
    data_abaut_user = [message.from_user.id, message.from_user.first_name, message.from_user.username, message.text.replace('/it ', '')]
    date = str(datetime.datetime.now())
    date = date[0 : date.rfind('.')-1]
    await log(data_abaut_user)
    if message.chat.id in config.CANNON_GROUP:
        await google.down_drive(data_abaut_user[3], date)
        process_id = erp.create_process(data_abaut_user, config.DOG_AND_ID_GROUP[message.chat.id])
        await bot.send_message(message.chat.id, 'Запрос был зафиксирован')
        await bot.send_message(config.CANNON_GROUP[0], f'Процесс был создан из группы {config.NAME_GROUP[message.chat.id]}, номер процесса\nhttp://erp.core.ufanet.ru/user/process#{process_id}')
    elif erp.authentications(message.from_user.id):
        process_id = erp.create_process(data_abaut_user, '')
        await bot.send_message(config.CANNON_GROUP[0], f'Процесс был создан не из группы посмотри в логах на негодяя, номер процесса\nhttp://erp.core.ufanet.ru/user/process#{process_id}')



# Регистрируем комманды
def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(report_in_google_sheets, commands=['it'])


# Логирование в гугл диск
async def log(log_text):
    date = str(datetime.datetime.now())
    date = date[0 : date.rfind('.')-1]
    await google.main_google(date, log_text[0], log_text[1], log_text[2], log_text[3], config.SHEETS_LOG)