import pyautogui
import time

# get the mouse coordinates
print(pyautogui.position())

# move to mouse coordinates, here is Google search bar
pyautogui.moveTo(677, 468)
pyautogui.click()

# if you want double click try this
# pyautogui.doubleClick()
# pyautogui.click(clicks=2, interval=1)

time.sleep(1)

# write your search word
pyautogui.typewrite("hello")
pyautogui.typewrite(['enter'])
