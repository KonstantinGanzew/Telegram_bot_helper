import config
from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.middlewares.logging import LoggingMiddleware

bot = Bot(config.TOKKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())