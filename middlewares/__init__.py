#-*- coding: utf-8 -*-

from aiogram import Dispatcher

from loader import dp
from .throttling import ThrottlingMiddleware
from .logger import UpdateLoggerMiddleware


if __name__ == "middlewares":
    dp.middleware.setup(UpdateLoggerMiddleware())
    dp.middleware.setup(ThrottlingMiddleware())