import asyncio
import time

import pyautogui


def Fletta():
    pyautogui.moveTo(x=1777, y=1030, duration=0.3)
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    pyautogui.moveTo(x=595, y=268, duration=0.3)
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    pyautogui.moveTo(x=472, y=311, duration=0.3)
    pyautogui.mouseDown()
    pyautogui.mouseUp()


def Rocas():
    x = 1591
    y = 207
    for i in range(5):
        pyautogui.moveTo(x=1577, y=280, duration=0.3)
        pyautogui.mouseDown()
        pyautogui.mouseUp()
        pyautogui.moveTo(x=x, y=y, duration=0.3)
        pyautogui.mouseDown()
        pyautogui.mouseUp()
        pyautogui.moveTo(x=910, y=610, duration=0.3)
        pyautogui.mouseDown()
        pyautogui.mouseUp()
        time.sleep(20)
        x += 36
