from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver import FirefoxOptions

import time

start = time.time()
print('_____start____programm____')

opts = FirefoxOptions()
opts.add_argument("--headless")

driver = webdriver.Firefox(executable_path = './utils/geckodriver', options=opts)

driver.get("http://www.python.org")
driver.quit()


print('_____finish____programm____')
print('work_time=', round(time.time()-start, 2), 'seconds')
