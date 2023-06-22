from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

class TestLogin:

    def setup_class(self):
        global driver
        driver = webdriver.Chrome()
        driver.maximize_window()

    def test_login(self):
            #define qual page o browser deve abrir
            driver.get('https://github.com/')

            btn_link_sign_in = driver.find_element (By.CLASS_NAME, 'HeaderMenu-link--sign-in')
            btn_link_sign_in.click()

            #realizamos uma captura de tela
            driver.save_screenshot('screen_01.png')

            #aguarda dois segundos
            time.sleep(2)

            field_login = driver.find_element(By.ID, 'login_field')
            field_login.send_keys('delnerotoni@gmail.com')

            field_password = driver.find_element(By.ID, 'password')
            field_password.send_keys('@Higgsbytes39')

            #realizamos uma captura de tela
            driver.save_screenshot('screen_02.png')

            field_password.send_keys(Keys.RETURN)

            #aguarda dois segundos
            time.sleep(2)


    def teardown_class(self):
        driver.close()