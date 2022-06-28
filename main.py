from concurrent.futures import process
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
    if message.chat.id in canon_groups:
        await bot.send_message(message.chat.id, 'Бот для переноса всех запросов в гугл таблицу, для отправки сообщения необходимо написать /it и текст сообщения')
    if erp.authentications(message.from_user.id):
        await bot.send_message(message.from_user.id, 'Добро пожаловать на галеру фраерок...')


# Отправляет сообщение на гугл диск и создает процесс в ответ на команду /it
async def report_in_google_sheets(message: types.Message):
    if message.chat.id in canon_groups:
        date = str(datetime.datetime.now())
        date = date[0 : date.rfind('.')-1]
        await google.down_drive(message.text.replace('/it ', ''), date)
        erp.create_process(message.text)
        await bot.send_message(message.chat.id, 'Сообщение было добавлино в гугл таблицу с указанием времени')
    if erp.authentications(message.from_user.id):
        process_id = erp.create_process(message.text.replace('/it ', ''))
        await bot.send_message(message.from_user.id, f'Процесс был создан номер процесса {process_id}')


# Регистрируем комманды
def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(report_in_google_sheets, commands=['it'])