import pyautogui
import time

def clicar_no_botao():
    tentativas = 5

    for _ in range(tentativas):
        try:
            box_botao = pyautogui.locateOnScreen('explorer.png')
            x, y = pyautogui.center(box_botao)
            pyautogui.click(x,y)
            break
        except pyautogui.ImageNotFoundException:
            print('Imagem não encontrada... vou tentar de novo')
            time.sleep(1)
    
time.sleep(5)
clicar_no_botao()





pyautogui.click('botao8.png')