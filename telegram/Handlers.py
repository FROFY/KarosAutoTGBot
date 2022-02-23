import time

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.dispatcher.filters import Text, Command

import pyautogui

import Config
import Methods
import telegram.Keyboards
import asyncio
from telegram.States import StatesBot

bot = Bot(Config.bot_token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
isActive = True


@dp.message_handler(commands=['start'], state=None)
async def start(message: types.Message):
    await bot.send_message(message.from_user.id, 'Made by FROFY', reply_markup=telegram.Keyboards.keyboard_main)


@dp.message_handler(Text(equals='📊 Прислать скриншот', ignore_case=True), state=None)
async def send_screenshot(message: types.Message):
    shot = pyautogui.screenshot()
    shot.save('shot.png')
    await bot.send_document(message.from_user.id, open('shot.png', 'rb'), caption='Текущий экран')


@dp.message_handler(Text(equals='🔽 Главное меню', ignore_case=True), state=None)
async def main_menu(message: types.Message):
    await bot.send_message(message.from_user.id, 'Main Menu', reply_markup=telegram.Keyboards.keyboard_main)


@dp.message_handler(Text(equals='Дополнительно', ignore_case=True), state=None)
async def main_menu(message: types.Message):
    await bot.send_message(message.from_user.id, 'Дополнительные настройки', reply_markup=telegram.Keyboards.keyboard_add)


@dp.message_handler(Text(equals='🔁 Слить флетту', ignore_case=True), state=None)
async def main_menu(message: types.Message):
    Methods.Fletta()
    await bot.send_message(message.from_user.id, 'Флетта слита')


@dp.message_handler(Text(equals='Статус противника', ignore_case=True), state=None)
async def main_menu(message: types.Message):
    shot = pyautogui.locateOnScreen('target.png', region=(850, 10, 240, 50), confidence=0.3)
    # shot = pyautogui.locateOnScreen('target.png', region=(850, 10, 240, 50), confidence=0.2)
    if shot is None:
        shot = 'None'

    await bot.send_message(message.from_user.id, shot)


@dp.message_handler(Text(equals='Остановить бота', ignore_case=True), state=None)
async def main_menu(message: types.Message):
    isActive = False
    await bot.send_message(message.from_user.id, 'Бот остановлен')


@dp.message_handler(Text(equals='Настройки бота', ignore_case=True), state=None)
async def main_menu(message: types.Message):
    await bot.send_message(message.from_user.id, 'Настройки бота', reply_markup=telegram.Keyboards.keyboard_bot)


@dp.message_handler(Text(equals='Запустить бота', ignore_case=True), state=None)
async def main_menu(message: types.Message):
    await bot.send_message(message.from_user.id, 'Запущен')
    while True:
        Methods.Fletta()
        # time.sleep(1)
        # Methods.Rocas()
        time.sleep(300)


"""@dp.message_handler(Text(equals='Запустить бота', ignore_case=True), state=None)
async def main_menu(message: types.Message):
    await bot.send_message(message.from_user.id, 'Бот запущен')
    while isActive:
        if not pyautogui.locateOnScreen('target.png', region=(850, 10, 240, 50), confidence=0.3):
            pyautogui.moveTo(x=415, y=1015, duration=0.1)
            pyautogui.mouseDown(button='right')
            pyautogui.mouseUp(button='right')
            pyautogui.moveTo(x=415, y=980, duration=0.1)
            pyautogui.mouseDown(button='right')
            pyautogui.mouseUp(button='right')
            pyautogui.moveTo(x=695, y=1015, duration=0.3)
            pyautogui.mouseDown(button='right')
            pyautogui.mouseUp(button='right')
            pyautogui.moveTo(x=730, y=1015, duration=0.3)
            pyautogui.mouseDown(button='right')
            pyautogui.mouseUp(button='right')
            await asyncio.sleep(3)
        else:
            await asyncio.sleep(1)
    await bot.send_message(message.from_user.id, 'Бот остановлен')
"""

@dp.message_handler(Text(equals='Включить духи', ignore_case=True), state=None)
async def main_menu(message: types.Message):
    pyautogui.moveTo(x=695, y=980, duration=0.2)
    pyautogui.mouseDown(button='right')
    pyautogui.mouseUp(button='right')
    pyautogui.mouseDown(button='left', x=912, y=610, duration=0.5)
    pyautogui.mouseUp(button='left', x=912, y=610, duration=0.5)
    await asyncio.sleep(0.5)
    pyautogui.moveTo(x=730, y=986, duration=0.2)
    pyautogui.mouseDown(button='right')
    pyautogui.mouseUp(button='right')
    pyautogui.mouseDown(button='left', x=912, y=610, duration=0.5)
    pyautogui.mouseUp(button='left', x=912, y=610, duration=0.5)

    await bot.send_message(message.from_user.id, 'Духи включены')

