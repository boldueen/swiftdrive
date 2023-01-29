from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver import FirefoxOptions

from utils.process.excel_and_csv_worker import create_daily_report_from_file
from utils.process.swift_browser import download_report_file

import time

start = time.time()
print('_____start____programm____')

# opts = FirefoxOptions()
# opts.add_argument("--headless")

# driver = webdriver.Firefox(executable_path = './utils/geckodriver', options=opts)

# driver.quit()
# yesterday, day_before_yesterday, first_day_of_month

# download_report_file(start_date='2023-01-27', end_date='2023-01-28', base_or_proj='BASE')
# download_report_file(start_date='2023-01-01', end_date='2023-01-28', base_or_proj='PROJ')

create_daily_report_from_file(filepath='utils/process/reports/daily_report.xlsx')

print('_____finish____programm____')
print('work_time:', round(time.time()-start, 2), 'seconds')
