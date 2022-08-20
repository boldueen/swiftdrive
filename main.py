from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import time

start = time.time()
print('_____start____programm____')



driver = webdriver.Firefox(executable_path = './utils/geckodriver')

driver.get("http://www.python.org")



titles = driver.find_elements(By.TAG_NAME, 'a')

for title in titles:
    print(title.text)

driver.quit()




print('_____finish____programm____')
print('work_time=', round(time.time()-start, 2), 'seconds')
