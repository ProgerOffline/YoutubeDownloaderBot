#-*- coding: utf-8 -*-

from aiogram import types
from loader import dp
from keyboards import ctypes


@dp.callback_query_handler(ctypes.download_format.filter(format="video"))
async def choose_vide_quality(call: types.CallbackQuery, callback_data: dict):
    pass

@dp.callback_query_handler(ctypes.download_format.filter(format="audio"))
async def get_video_link(call: types.CallbackQuery, callback_data: dict):
    pass

@dp.callback_query_handler(ctypes.info)
async def show_bot_functions(call: types.CallbackQuery, callback_data: dict):
    pass