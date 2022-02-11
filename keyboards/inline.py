#-*- coding: utf-8 -*-

from aiogram import types
from keyboards import ctypes

def main_menu():
    return types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(
            text="ℹ️  Возможности",
            callback_data=ctypes.info.new(),
        )
    ).add(
        types.InlineKeyboardButton(
            text="🖥  Загрузить видео",
            callback_data=ctypes.download.new(format="video"),
        ),
        types.InlineKeyboardButton(
            text="🎧  Загрузить музыку",
            callback_data=ctypes.download.new(format="audio"),
        ),
    )
