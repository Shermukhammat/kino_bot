from aiogram import Dispatcher
from aiogram.dispatcher.middlewares import BaseMiddleware

from loader import dp
from .midle_checksub import  Bro
from .throttling import ThrottlingMiddleware

if __name__ == 'middlewares':
    dp.middleware.setup(ThrottlingMiddleware())
    dp.middleware.setup(Bro())