from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

#функция понадобится для расчета математического выражения
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
	browser = webdriver.Chrome()

	browser.get("http://suninjuly.github.io/explicit_wait2.html")

	# говорим Selenium проверять в течение 12 секунд, пока цена не станет $100
	cost = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), '$100'))
	
	#нажимаем кнопку book
	option1 = browser.find_element_by_id("book").click()

	#скролим страницу до математического выражения
	field = browser.find_element_by_id("input_value")
	browser.execute_script("return arguments[0].scrollIntoView(true);", field)
	
	#решаем математическое выражение
	x = browser.find_element_by_id('input_value').text
	y = calc(x)

	#вставляем решение в тестовое поле
	input1 = browser.find_element_by_id('answer').send_keys(y)
	

	#нажимаем кнопку submit
	option2 = browser.find_element_by_id('solve').click()

finally:
	# ожидание чтобы визуально оценить результаты прохождения скрипта
	time.sleep(10)
	# закрываем браузер после всех манипуляций
	browser.quit()