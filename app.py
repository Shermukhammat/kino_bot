from aiogram import executor
from loader import dp
import handlers
import middlewares
import logging

if __name__ == "__main__":

    # logging.basicConfig()
    executor.start_polling(dp, skip_updates = False)
    