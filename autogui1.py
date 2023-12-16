import pyautogui

largura, altura = pyautogui.size()
print(largura, altura)

mousex, mousey = pyautogui.position()

print(mousex, mousey)

pyautogui.moveTo(1388, 1751)
pyautogui.click()
