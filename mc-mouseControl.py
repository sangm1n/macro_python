# simple macro practice in python by sangmin

import pyautogui
import time

# get the mouse coordinates
print(pyautogui.position())

# use to mouse coordinates and move, this example is Google search bar
pyautogui.moveTo(677, 468)
pyautogui.click()

# if you want double click, try this
# pyautogui.doubleClick()
# pyautogui.click(clicks=2, interval=sec)

time.sleep(1)

# write your search word
pyautogui.typewrite("install python")
pyautogui.typewrite(['enter'])
