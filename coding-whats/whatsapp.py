import pyautogui
import time

time.sleep(3)
for i in range(100):
    pyautogui.typewrite("hello world")
    pyautogui.press("Enter")
