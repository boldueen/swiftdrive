from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver import FirefoxOptions, FirefoxProfile
from selenium.webdriver.firefox.options import Options
from settings import PASSWORD, DOWNLOAD_PATH, LOGIN, FILEPATH, PWD
import time
import os
from halo import Halo





def download_report_file(start_date:str, end_date:str):
    """
    start_date example: '2022-03-23'
    """
    opts = FirefoxOptions()
    # opts.add_argument("--headless")

    delete_file(FILEPATH)

    opts.set_preference("browser.download.folderList", 2)
    opts.set_preference("browser.download.manager.showWhenStarting", False)
    opts.set_preference("browser.download.dir", DOWNLOAD_PATH)
    opts.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/x-gzip")


    # driver = webdriver.Firefox(executable_path = './utils/geckodriver', options=opts, firefox_profile=profile)
    driver = webdriver.Firefox(executable_path = './utils/geckodriver', options=opts)

    spinner = Halo(text='open url', spinner='simpeDots')
    spinner.start()
    driver.get('https://swiftdrive.ru/auth/signin')
    spinner.stop()
    spinner.info("url open!")

    time.sleep(2)

    spinner = Halo(text='authorizing', spinner='dots')
    spinner.start()

    email = driver.find_element(By.XPATH, "/html/body/div/div/div[1]/div/div/div[2]/form/fieldset/div[1]/div/div/input")

    password = driver.find_element(By.XPATH,
                                    "/html/body/div/div/div[1]/div/div/div[2]/form/fieldset/div[2]/div/div/input")

    email.send_keys(LOGIN)
    password.send_keys(PASSWORD)

    button = driver.find_element(By.XPATH, '//*[@id="app-site"]/div/div[1]/div/div/div[2]/form/fieldset/div[3]/button')
    button.click()

    spinner.stop()
    spinner.info("authorizing complete")

    driver.get('https://swiftdrive.ru/app/customers-reports')
    time.sleep(1)

    driver.find_element(By.XPATH, '//*[contains(text(), "Диапазон")]').click()





    start_date_webelement = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/div[1]/div/div/input')
    start_date_webelement.send_keys(start_date)

    end_date_webelement = driver.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/div[2]/div/div/input')
    end_date_webelement.send_keys(end_date)

    driver.find_element(By.XPATH, '//*[contains(text(), "Применить")]').click()


    driver.find_element(By.XPATH, '//*[contains(text(), "Экспорт")]').click()
    driver.find_element(By.XPATH, '//*[contains(text(), "Экспортировать")]').click()

    while True:
        if os.path.isfile(FILEPATH):
            print('...file successfully downloaded...')
            break

    time.sleep(1)

    driver.quit()

    return True


def delete_file(path: str = FILEPATH) -> bool:
    try:
        os.remove(path)
    except:
        pass
    if os.path.isfile(path):
        return False
    return True













