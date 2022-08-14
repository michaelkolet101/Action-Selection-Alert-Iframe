import time
import logging
from telnetlib import EC
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

logging.basicConfig(level=logging.INFO)
mylogger = logging.getLogger()

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrom_driver_path = "/home/michael/seleln/chromedriver"


def test_drag_and_drop():

    driver = webdriver.Chrome(chrom_driver_path, chrome_options=chrome_options)
    driver.get('https://demo.guru99.com/test/drag_drop.html')
    driver.set_window_size(800, 800)
    mylogger.info("test for drag drop")

    action = ActionChains(driver)

    block_button = driver.find_element(By.CLASS_NAME, "block13 ")
    button_5000 = block_button.find_element(By.CLASS_NAME, "button")
    drop1 = driver.find_element(By.ID, "shoppingCart4")
    action.drag_and_drop(button_5000, drop1).perform()

    button_bank = driver.find_element(By.ID, "credit2")
    shopping_card = driver.find_element(By.ID, "shoppingCart1")
    drop2 = shopping_card.find_element(By.CLASS_NAME, "ui-widget-content")
    action.drag_and_drop(button_bank, drop2).perform()

    drop4 = driver.find_element(By.ID, "amt8")
    action.drag_and_drop(button_5000, drop4).perform()

    button_c = driver.find_element(By.ID, "credit1")
    drop3 = driver.find_element(By.ID, "shoppingCart3").find_element(By.ID, "loan")
    action.drag_and_drop(button_c, drop3).perform()

    result_table = driver.find_element(By.CLASS_NAME, "table4_result")
    result_button = result_table.find_element(By.CLASS_NAME, "button")
    result_button.click()

    time.sleep(5)
    driver.quit()


def test_to_iframe():

    my_email = 'michael101@gmail.com'
    my_password = '12345'

    driver = webdriver.Chrome(chrom_driver_path, chrome_options=chrome_options)
    driver.get('http://automationpractice.com/index.php')
    driver.set_window_size(800, 800)
    mylogger.info("test iframe")
    container = driver.find_element(By.CLASS_NAME, "product-container")
    container.find_element(By.CLASS_NAME, 'icon-eye-open').click()

    # switch_to frame
    driver.switch_to.frame(driver.find_element(By.CLASS_NAME, "fancybox-iframe"))
    time.sleep(3)
    add_to_card = driver.find_element(By.ID, "add_to_cart")
    add_to_card.click()
    time.sleep(3)

    button = driver.find_element(By.CLASS_NAME, "button-container")
    button.find_element(By.CLASS_NAME, "btn.btn-default.button.button-medium").click()
    time.sleep(3)
    button = driver.find_element(By.CLASS_NAME, "cart_navigation.clearfix")
    button.find_element(By.CLASS_NAME, "button.btn.btn-default.standard-checkout.button-medium").click()
    time.sleep(3)

    driver.find_element(By.ID, "email").send_keys(my_email)
    driver.find_element(By.ID, "passwd").send_keys(my_password)
    driver.find_element(By.CLASS_NAME, "icon-lock").click()
    time.sleep(3)

    driver.find_element(By.CSS_SELECTOR, '[name=processAddress]').click()
    time.sleep(2)

    driver.find_element(By.CSS_SELECTOR, '[type=checkbox]').click()
    time.sleep(2)

    driver.find_element(By.CSS_SELECTOR, '[name=processCarrier]').click()
    time.sleep(2)

    driver.find_element(By.CLASS_NAME, "bankwire").click()
    time.sleep(2)

    driver.find_element(By.CSS_SELECTOR, "button.button-medium").click()
    time.sleep(2)

    comp = driver.find_element(By.CLASS_NAME, "cheque-indent").find_element(By.CLASS_NAME, "dark")
    assert "Your order on My Store is complete." in comp.text

    time.sleep(5)
    driver.close()



def test_for_alerts():
    driver = webdriver.Chrome(chrom_driver_path, chrome_options=chrome_options)
    driver.get('http://the-internet.herokuapp.com/javascript_alerts')
    driver.set_window_size(800, 800)
    mylogger.info("test for alerts")
    result = driver.find_element(By.ID, "result")
    result_list = []
    example = driver.find_element(By.CLASS_NAME, 'example')
    buttons = example.find_elements(By.TAG_NAME, 'button')
    for btn in buttons:
        btn.click()
        alert = driver.switch_to.alert
        if 'prompt' in alert.text:
            alert.send_keys("Michael Kolet")
        time.sleep(2)
        alert.accept()
        result_list.append(result.text)
        time.sleep(2)

    assert result_list[0] == "You successfully clicked an alert"
    assert result_list[1] == "You clicked: Ok"
    assert result_list[2] == "You entered: Michael Kolet"

    time.sleep(3)
    driver.quit()


def test_selection_register():
    driver = webdriver.Chrome(chrom_driver_path, chrome_options=chrome_options)
    driver.get('https://demo.guru99.com/test/newtours/register.php')
    driver.set_window_size(800, 800)
    mylogger.info("test for selection register")
    driver.find_element(By.NAME, "firstName").send_keys("Michael")
    driver.find_element(By.NAME, "lastName").send_keys("Kolet")
    driver.find_element(By.NAME, "phone").send_keys("05077766654")
    driver.find_element(By.NAME, "userName").send_keys("michael101")
    driver.find_element(By.NAME, "address1").send_keys("htidhr 14")
    driver.find_element(By.NAME, "city").send_keys("mega")
    driver.find_element(By.NAME, "state").send_keys("banana")
    driver.find_element(By.NAME, "postalCode").send_keys("121212")
    # do the select
    select_country = driver.find_element(By.NAME, "country")
    select = Select(select_country)
    select.select_by_value("ISRAEL")

    driver.find_element(By.NAME, "email").send_keys("michael101@gmail.com")
    driver.find_element(By.NAME, "password").send_keys("123456")
    confirm_password = driver.find_element(By.NAME, "confirmPassword")
    confirm_password.send_keys("123456")
    confirm_password.send_keys(Keys.ENTER)
    time.sleep(2)
    res = driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(5) > table > tbody > tr > td:nth-child(2) > table > tbody > tr:nth-child(4) > td > table > tbody > tr > td:nth-child(2) > table > tbody > tr:nth-child(3) > td > p:nth-child(2) > font")

    assert "Thank you for registering" in res.text
    time.sleep(5)
    driver.quit()