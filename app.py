from aiogram import executor
from loader import dp
import handlers
import middlewares

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = False)
    