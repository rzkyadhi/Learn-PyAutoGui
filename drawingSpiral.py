import pyautogui
import time

time.sleep(1)
distance = 300

pyautogui.moveTo(300, 300)

while distance>0:
    pyautogui.dragRel(distance, 0, 1, button="left")
    distance = distance - 20
    pyautogui.dragRel(0, distance, 1, button="left")
    pyautogui.dragRel(-distance, 0, 1, button="left")
    distance = distance - 20
    pyautogui.dragRel(0, -distance, 1, button="left")
    time.sleep(4)

