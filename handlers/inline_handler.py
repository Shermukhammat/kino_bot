from aiogram import types

from loader import db, dp, ram


@dp.inline_handler()

async def search(query : types.InlineQuery):
    text = query.query

    indexs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    answers = []
    n = 0

    for index in indexs:
        answers.append(types.InlineQueryResultArticle(id = str(n), 
                                                        title = f'Bu yerda kino {index} title si bo\'ladi',
                                                        #   thumb_url = "AAMCBAADGQEAAhkEZINYvRyHAdx3i3WIkCMpcamOMQQAAgkeAAI_vRhTWdHNQuX71tQBAAdtAAMvBA",
                                                        thumb_url = "https://telegra.ph/file/a7112f8f0763f8e4b22d5.jpg",
                                                        input_message_content = types.InputTextMessageContent(message_text = f"/get {index}")))
        n+=1

    await query.answer(answers)