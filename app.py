from aiogram import executor
from loader import dp
import handlers


if __name__ == "__main__":
    print("...")
    executor.start_polling(dp, skip_updates = False)