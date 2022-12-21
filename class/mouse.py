import pyautogui
import time

pyautogui.FAILSAFE = False
while True:
    time.sleep(5)
    print("wake")
    for i in range(0,100):
        pyautogui.moveTo(0,i*5)


