from loader import types, dp, db, ram, dbuttons, ibuttons



@dp.message_handler()
async def core_message_handler(message : types.Message):
    id = message.from_user.id

    if ram.check_user(id):
        # {'name': 'SHermukhammad', 'lang': 'uz', 'where': 'none', 'action': 'none', 'registred': '17.07.2023 13:47'}
        user = ram.get_info(id)
        name = user['name']
        where = user['where']

        if user['where'] == 'none':
            user['where'] = 'head_menu'
            await message.answer(f"Foydalanuvchi : {user['name']}\nRo'yxatdan o'tdi : {user['registred']}", reply_markup = dbuttons.menu())



        elif user['where'] == 'head_menu':
            if message.text == '🎛 Menu':
                await message.answer(f"📓 Bosh menu:\n\nFoydalanuvchi : {user['name']}\nRo'yxatdan o'tdi : {user['registred']}", reply_markup = ibuttons.menu())


            if user['action'] == 'sign_admin':
                count = ram.bloc_user(id)
                if count <= 2:
                    if message.text == '1234':
                        user['action'] = 'none'
                        ram.registr(id = id, name = user['name'], admin = True)
                        await message.reply("Admin aka ush kelibsiz")
                    else:
                        await message.reply(f"Xato sizda {3 - count} urunish qoldi")
                elif count == 3:
                    if message.text == '1234':
                        user['action'] = 'none'
                        ram.registr(id = id, name = user['name'], admin = True)
                        await message.reply("Admin aka ush kelibsiz ")
                    else:
                        user['action'] = 'none'
                        await message.reply("Ko'd xato bloklanding")
                    
            
    elif ram.check_admin(id):
        admin = ram.get_info(id, admin = True)
        name = admin['name']
        where = admin['where']

        if admin['where'] == 'none':
            admin['where'] = 'head_menu'
            await message.answer(f"Admin : {admin['name']}\nRo'yxatdan o'tdi : {admin['registred']}", reply_markup = dbuttons.menu())



        elif admin['where'] == 'head_menu':
            if message.text == '🎛 Menu':
                await message.answer(f"📓 Bosh menu:\n\nAdmin : {admin['name']}\nRo'yxatdan o'tdi : {admin['registred']}", reply_markup = ibuttons.menu())      

    else:
        pass
    