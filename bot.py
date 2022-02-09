#-*- coding: utf-8 -*-

from aiogram import executor
import middlewares, handlers

from loader import dp

async def on_startup(dispatcher):
    pass

if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup)