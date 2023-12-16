import pyautogui

pyautogui.alert(text='O nome digitado foi errado', title='Erro!', button='OK')

x = pyautogui.confirm(text='Você quer apagar mesmo o registo', title='Aviso!', buttons=['Sim', 'Não'])
print(x)

y = pyautogui.prompt(text='Digite seu nome', title='Nome do Usuário' , default='')
print(y)

pyautogui.password(text='', title='', default='', mask='*')