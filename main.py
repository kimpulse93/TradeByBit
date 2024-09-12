import asyncio
import logging

import pybit
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types import ReplyKeyboardMarkup
from fontTools.misc.cython import returns

from pybit.unified_trading import HTTP
from pybit import exceptions

from config import API_KEY, SECRET_KEY, TOKEN


def aio():
    cl = HTTP(
        #recv_window=60000,
        api_secret=SECRET_KEY,
        api_key=API_KEY,

    )
    a = cl.get_spot_asset_info(
        accountType="FUND",
        coin="USDC",
    )
    print(a)
    return cl






    #
    # try:
    #     r = cl.get_orderbook(category="linear", limit=10)
    #     print(r)
    #
    # except exceptions.InvalidRequestError as e:
    #     print("ByBit Request Error", e.status_code, e.message, sep=" | ")
    # except exceptions.FailedRequestError as e:
    #     print("ByBit Request Failed", e.status_code, e.message, sep=" | ")
    # except Exception as e:
    #     print(e)


# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token=TOKEN)
# Диспетчер
dp = Dispatcher()

kb = [
    [types.KeyboardButton(text="/balance")],
    [types.KeyboardButton(text="Лимитки")],
    [types.KeyboardButton(text="Закрыть лимитки")],
    [types.KeyboardButton(text="Позиции")],
    [types.KeyboardButton(text="Закрыть позиции")],

]

kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, keyboard=kb)


# Хэндлер на команду /start

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!", reply_markup=kb_client)

# @dp.message(Command("balance"))
# async def balance():



# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    aio()
    asyncio.run(main())
