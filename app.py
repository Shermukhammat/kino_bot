from aiogram import executor
from loader import dp
import handlers
3

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = False)
    