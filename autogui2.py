import pyautogui
import time

pyautogui.press('win')
time.sleep(1)
pyautogui.write('paint')
time.sleep(2)
pyautogui.press('enter')
time.sleep(10)
pyautogui.hotkey('win', 'up')
pyautogui.moveTo(1440,900)
distance = 200
while distance > 0:
    pyautogui.drag(distance, 0, duration=0.5)   # move right
    distance -= 5
    pyautogui.drag(0, distance, duration=0.5)   # move down
    pyautogui.drag(-distance, 0, duration=0.5)  # move left
    distance -= 5
    pyautogui.drag(0, -distance, duration=0.5)  # move up


