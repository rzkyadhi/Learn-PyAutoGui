import pyautogui
import time

time.sleep(3)

for i in range(10):
    pyautogui.moveTo(430, 390)
    time.sleep(2)
    pyautogui.doubleClick()
    time.sleep(2)
    pyautogui.moveTo(783, 414)
    time.sleep(1)
    pyautogui.leftClick()

