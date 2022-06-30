import config
import datetime
import erp
from aiogram import types, Dispatcher
from create_bot import bot
from googleDisk import google


# Авторизованные группы
canon_groups = [-603892836,
                -618154662]


# Отвечает на команду старт
async def command_start(message: types.Message):
    await log([message.from_user.id, message.from_user.first_name, message.from_user.username, message.text.replace('/it ', '')])
    if message.chat.id in canon_groups:
        await bot.send_message(message.chat.id, 'Бот для переноса всех запросов в гугл таблицу, для отправки сообщения необходимо написать /it и текст сообщения')
    if erp.authentications(message.from_user.id):
        await bot.send_message(message.from_user.id, 'Добро пожаловать на галеру фраерок...')


# Отправляет сообщение на гугл диск и создает процесс в ответ на команду /it
async def report_in_google_sheets(message: types.Message):
    data_abaut_user = [message.from_user.id, message.from_user.first_name, message.from_user.username, message.text.replace('/it ', '')]
    date = str(datetime.datetime.now())
    date = date[0 : date.rfind('.')-1]
    await log(data_abaut_user)
    if message.chat.id in canon_groups:
        await google.down_drive(data_abaut_user[3], date)
        erp.create_process(data_abaut_user)
        await bot.send_message(message.chat.id, 'Сообщение было добавлино в гугл таблицу с указанием времени')
    elif erp.authentications(message.from_user.id):
        process_id = erp.create_process(data_abaut_user)
        await bot.send_message(message.from_user.id, f'Процесс был создан номер процесса {process_id}')


# Регистрируем комманды
def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(report_in_google_sheets, commands=['it'])


# Логирование в гугл диск
async def log(log_text):
    date = str(datetime.datetime.now())
    date = date[0 : date.rfind('.')-1]
    await google.main_google(date, log_text[0], log_text[1], log_text[2], log_text[3], config.SHEETS_LOG)