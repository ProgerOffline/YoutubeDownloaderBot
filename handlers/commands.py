#-*- coding: utf-8 -*-

from aiogram import types
from loader import dp

@dp.message_handler(commands=['start'], state=None)
async def cmd_start(message: types.Message):
    await message.answer("Привет, я еще в разработке...")