#-*- coding: utf-8 -*-

import keyboards

from aiogram import types
from loader import dp


@dp.message_handler(commands=['start'], state=None)
async def cmd_start(message: types.Message):
    await message.answer(
        text="👋 Приветствую в <b>Youtube Загрузчике</b>",
        reply_markup=keyboards.main_menu(),
    )