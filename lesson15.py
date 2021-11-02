from selenium import webdriver
import time
import math


link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)


    button = browser.find_element_by_tag_name("button")
    button.click()
    
    confirm=browser.switch_to.alert
    confirm.accept()
    
    x1 = browser.find_element_by_id('input_value')
    x = x1.text
    y=str(math.log(abs(12*math.sin(int(x)))))
    
    input1 = browser.find_element_by_tag_name('input')
    input1.send_keys(y)
    
    
    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла