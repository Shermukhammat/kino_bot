from aiogram import Bot

async def check_sub(user_id : int, chanel : str):
    try:
        bot = Bot.get_current()
        await bot.get_chat_member(chat_id = chanel, user_id = user_id)

        return True
    except:
        return False