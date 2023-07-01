import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ChatPermissions
from datetime import timedelta

API_TOKEN = '6122101445:AAEetThID0yMzfbo-StrRvASFcQUo3clENw'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hello")


@dp.message_handler(text="!mute", is_chat_admin=True)
async def mute_user(message: types.Message):
    if message.chat.type in ["supergroup", "group"]:
        if not message.reply_to_message or not message.reply_to_message.from_user:
            await message.reply("Iltimos, biror kishini belgilab keyin komandani yuboring")
            return
        
        user_to_mute = message.reply_to_message.from_user
        await bot.restrict_chat_member(
            chat_id=message.chat.id,
            user_id=user_to_mute.id,
            permissions=ChatPermissions(
            can_send_messages=False,
            ),
            until_date=message.date + timedelta(minutes=30)
        )

        await message.reply(f"{user_to_mute.mention} 30 minutga ban")



@dp.message_handler(text="!unmute", is_chat_admin=True)
async def mute_user(message: types.Message):
    if message.chat.type in ["supergroup", "group"]:
        if not message.reply_to_message or not message.reply_to_message.from_user:
            await message.reply("Iltimos, biror kishini belgilab keyin komandani yuboring")
            return
        
        user_to_mute = message.reply_to_message.from_user
        await bot.restrict_chat_member(
            chat_id=message.chat.id,
            user_id=user_to_mute.id,
            permissions=ChatPermissions(
            can_send_messages=True,
            ),
            until_date=0
        )

        await message.reply(f"{user_to_mute.mention} mayli yoz")


@dp.message_handler(text="!ban", is_chat_admin=True)
async def mute_user(message: types.Message):
    if message.chat.type in ["supergroup", "group"]:
        if not message.reply_to_message or not message.reply_to_message.from_user:
            await message.reply("Iltimos, biror kishini belgilab keyin komandani yuboring")
            return
        
        user_to_kick = message.reply_to_message.from_user
        await bot.kick_chat_member(
            chat_id=message.chat.id,
            user_id=user_to_kick.id,
        )

        await message.reply(f"{user_to_kick.mention} chopildin")


@dp.message_handler(text="!unban", is_chat_admin=True)
async def mute_user(message: types.Message):
    if message.chat.type in ["supergroup", "group"]:
        if not message.reply_to_message or not message.reply_to_message.from_user:
            await message.reply("Iltimos, biror kishini belgilab keyin komandani yuboring")
            return
        
        user_to_unban = message.reply_to_message.from_user
        await message.chat.unban(user_to_unban.id)

        await message.reply(f"{user_to_unban.mention} mayli kir")




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)