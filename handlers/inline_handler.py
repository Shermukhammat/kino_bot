from aiogram import types
import uuid
from loader import db, dp, ram, google


@dp.inline_handler()



async def search(message : types.InlineQuery):
    if len(message.query) > 1:
        indexs = google.search_movies(match = message.query, limt = 3)
        
        answers = []
        for index in indexs:
            movi = ram.movies[index]
            answers.append(types.InlineQueryResultArticle(id = str(uuid.uuid4()), 
                                                        title = movi['title'],
                                                        description = f"xajmi : {movi['size']} mb| davomiyligi : {movi['duration']} | tili : {movi['lang']}",
                                                        #   thumb_url = "AAMCBAADGQEAAhkEZINYvRyHAdx3i3WIkCMpcamOMQQAAgkeAAI_vRhTWdHNQuX71tQBAAdtAAMvBA","https://telegra.ph/file/a7112f8f0763f8e4b22d5.jpg"
                                                        thumb_url = movi['thum_url'],
                                                        input_message_content = types.InputTextMessageContent(message_text = f"/get {index}")))
        

        await message.answer(answers)
    
    

if __name__ == '__main__':
    pass