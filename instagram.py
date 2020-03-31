from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time
credentials = {
    "username": "",
    "password": "",
}

userList = ["juniordev.js"]
driver = webdriver.Chrome("/home/juniordev/Downloads/chromedriver")
driver.implicitly_wait(10)


def open_instagram():
    driver.get("http://instagram.com")
    username = driver.find_element_by_name("username")
    print("user: {}".format(username))
    username.send_keys(credentials["username"])
    password = driver.find_element_by_name("password")
    password.send_keys(credentials["password"])
    password.send_keys(Keys.RETURN)
    time.sleep(3)
    for user in userList:
        driver.get("http://instagram.com/{}/?hl=pt-br".format(user))
        fotos = driver.find_elements_by_css_selector('article > div img[decoding="auto"]')
        time.sleep(3)
        for foto in fotos:
            ActionChains(driver).move_to_element(foto).click().perform()
            time.sleep(1)
            curtida = driver.find_element('span[aria-label="Curtir"][class="glyphsSpriteHeart__outline__24__grey_9 u-__7"]')

open_instagram()
