from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("log-level=3")
driver = Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

driver.get("https://precos.petrobras.com.br/seleção-de-estados-gasolina")
elemento = driver.find_element(by=By.ID, value="telafinal-precofinal")
valor = elemento.text
print("Valor médio da gasolina no Brasil:", valor)
driver.quit()