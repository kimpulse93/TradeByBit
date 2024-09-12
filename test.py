import asyncio
import logging

import pybit
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types import ReplyKeyboardMarkup
from fontTools.misc.cython import returns

from pybit.unified_trading import HTTP
from pybit import exceptions

import bybit
from config import API_KEY, SECRET_KEY, TOKEN

from pybit.unified_trading import HTTP
session = HTTP(

    api_key=API_KEY,
    api_secret=SECRET_KEY,
)
print(session.get_wallet_balance(
    accountType="UNIFIED",
    coin="BTC",
))



