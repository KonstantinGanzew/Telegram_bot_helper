import datetime
from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Command, Text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from create_bot import dp, bot
from googleDisk import google


canon_groups = [-603892836,
                -618154662]

async def command_start(message: types.Message):
    if message.chat.id in canon_groups:
        await bot.send_message(message.chat.id, 'Бот для переноса всех запросов в гугл таблицу, для отправки сообщения необходимо написать /it и текст сообщения')


async def report_in_google_sheets(message: types.Message):
    if message.chat.id in canon_groups:
        date = str(datetime.datetime.now())
        date = date[0 : date.rfind('.')-1]
        await google.down_drive(message.text.replace('/it ', ''), date)
        await bot.send_message(message.chat.id, 'Сообщение было добавлино в гугл таблицу с указанием времени')

# Регистрируем комманды
def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(report_in_google_sheets, commands=['it'])