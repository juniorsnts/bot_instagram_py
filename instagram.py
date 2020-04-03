from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
credentials = {
    "username": "",
    "password": "",
}

userList = ["thediego_st"]
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
    time.sleep(6)
    for user in userList:
        print("Buscando o usuario: {}".format(user))
        driver.get("http://instagram.com/{}/".format(user))
        fotos = driver.find_elements_by_css_selector('article > div img[decoding="auto"]')
        print("Encontrei {} fotos".format(len(fotos)))
        for foto in fotos:
            ActionChains(driver).move_to_element(foto).click().perform()
            time.sleep(1)
            try:
                curtida = driver.find_element_by_css_selector('div button > svg[aria-label="Curtir"]')
                curtida.click()
                print('Curtir')
                driver.find_element_by_css_selector('div button > svg[aria-label="Fechar"]').click()
            except:
                print('Ja curtido')
                driver.find_element_by_css_selector('div button > svg[aria-label="Fechar"]').click()
        print('Finish')

open_instagram()
