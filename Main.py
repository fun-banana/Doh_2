from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import time

def main():
    '''Main.'''
    options = Options()
    options.headless = True
    driver = webdriver.Chrome() #chrome_options=options
    driver.get('https://one.prat.idf.il/login')
    time.sleep(3)
    element = driver.find_element(By.CLASS_NAME, 'formControl')
    element.send_keys("")
    element = driver.find_element(By.CLASS_NAME, 'btnGeneral')
    element.click()
    time.sleep(3)
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
    print(driver.title)
    time.sleep(5)
    element = driver.find_element(By.NAME, 'passwd')
    element.send_keys("")
    enter = driver.find_element(By.ID, 'idSIButton9')
    enter.click()
    time.sleep(10)



if __name__ == '__main__':
    main()