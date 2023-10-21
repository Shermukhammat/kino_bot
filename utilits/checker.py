from aiogram import Bot

async def check_sub(user_id : int, chanel : str):
    try:
        bot = Bot.get_current()
        member  = await bot.get_chat_member(chat_id = chanel, user_id = user_id)
        # print('-'*10)
        # print(chanel)
        # print(member)
        # print(member.is_chat_member())
        if member.status != 'left':
            return True
        return False
    except:
        return False