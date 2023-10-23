from aiogram import executor
from loader import dp, ram, bot
import handlers
import middlewares
import logging
from cfonts import render, say


async def on_startup(dp):
    print("Bot started : True")
    await bot.send_message(chat_id = 1661189380, text = "🏃 Bot started run") 


async def on_shutdown(dp):
    print("Bot started : False")
    await bot.send_message(chat_id = 1661189380, text = "😱 Bot stoped run")


if __name__ == "__main__":
    output = render('MoviBot.io', colors=['white', 'blue'], align = 'center')
    print(output)

    executor.start_polling(dp, skip_updates = False, on_startup = on_startup, on_shutdown = on_shutdown)
    