#-*- coding: utf-8 -*-

from aiogram import types


def main_menu():
    return types.InlineKeyboardMarkup().add(
        types.InlineKeyboardButton(
            text="ТЕст",
            callback_data="1",
        )
    )
