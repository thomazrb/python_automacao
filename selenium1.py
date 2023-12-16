from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.selenium.dev/selenium/web/web-form.html")
driver.implicitly_wait(0.5)
print(driver.title)

text_box = driver.find_element(by = By.NAME, value='my-text')
text_box.send_keys("Teste")

submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
submit_button.click()

message = driver.find_element(by=By.ID, value="message")
print(message.text)
input()
driver.quit()