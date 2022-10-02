import sys
import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from config import ROUTER_IP, ROUTER_USERNAME, ROUTER_PASSWORD, WAIT_TIME, GRID_ENDPOINT

logging.basicConfig(level=logging.INFO)

logging.info("Setting up driver")
driver = webdriver.Remote(
    command_executor=f"http://{GRID_ENDPOINT}/wd/hub", options=webdriver.ChromeOptions()
)

logging.info("Connecting to router homepage")
driver.get(f"http://{ROUTER_IP}/2.0/gui/#/login/")
driver.implicitly_wait(WAIT_TIME)

logging.info("Logging into UI")
username_field = driver.find_element(by=By.ID, value="name")
password_field = driver.find_element(by=By.ID, value="password")
login_button = driver.find_element(by=By.TAG_NAME, value="button")

username_field.send_keys(ROUTER_USERNAME)
password_field.send_keys(ROUTER_PASSWORD)
login_button.click()
time.sleep(WAIT_TIME)

home_section = driver.find_element(by=By.CLASS_NAME, value="welcome")
welcome_message = home_section.find_element(by=By.TAG_NAME, value="span")

if welcome_message.text != "Welcome to my gateway":
    logging.info("Router login failed, exiting")
    sys.exit(1)

logging.info("Connecting to router reboot page")
driver.get(f"http://{ROUTER_IP}/2.0/gui/#/mybox/maintenance/reset")
driver.implicitly_wait(WAIT_TIME)

reboot_button = driver.find_element(by=By.ID, value="restartGatewayTip")
reboot_button.click()
time.sleep(WAIT_TIME)

logging.info("Restarting router")
restart_modal = driver.find_element(by=By.ID, value="restart-modal")
confirm_button = driver.find_elements(by=By.TAG_NAME, value="button")[-1]
confirm_button.click()

logging.info("Router rebooted")
driver.quit()
