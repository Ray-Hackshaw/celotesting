# CELO Health master test script - Ray Hackshaw v1.1
# Test cases in this script are best accompanied by the test plan docs available on my Github @https://github.com/Ray-Hackshaw/celotesting

from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import unittest
import time


# Test initialisation
browser = webdriver.Chrome()
browser.maximize_window()
browser.get("https://stagingapp.celohealth.com")

    
def test_login():
    delay = 5
    try:
        login_button = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'login')))
        login_button.click()
        username = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'Username')))
        password = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'Password')))
        username.send_keys('CANDIDATE_EMAIL_WENT_HERE')
        time.sleep(1)
        password.send_keys('CANDIDATE_PASSWORD_WENT_HERE')
        sign_in_button = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div[1]/div/div/div[3]/div/form/fieldset/div[3]/button')))
        sign_in_button.click()
        time.sleep(1)
    except NoSuchElementException:
        print("Error: one or more login elements cannot be found.")
    except TimeoutException:
        print("Error: page [LOGIN] timed out.")
    except:
        print("There was an error with your login credentials. Please check them and try again. ")

def test_pin_codes_registration():
    pin = '5497'
    try:
        pin_number = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, 'pin_code')))
        pin_re = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="pin_code_confirm"]')))
        pin_number.send_keys(pin)
        time.sleep(1)
        pin_re.send_keys(pin)
        next_button = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/app-root/div/div/app-pinscreen/div[1]/div/div/div[3]/button")))
        next_button.click()
    except NoSuchElementException:
        print("Error: one or more pin code elements cannot be found.")
    except TimeoutException:
        print("Error: page [PIN_CODE_REGISTRATION] timed out.")
    except:
        print("There was an error with your pin code(s). Please check they have been entered correctly and try again.")

def test_send_message():
    try:
        message = "Automated test message."
        conversation_card = '//*[@id="conversations-scroll"]/div[2]/app-conversation-list/div/div[1]/a/app-conversation-card/div' #for existing top conversation
        time.sleep(1)
        existing_conversation = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, conversation_card)))
        existing_conversation.click()
        message_box = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.ID, "celo-send-message-textarea")))
        message_box.send_keys(message)
        message_box.send_keys(Keys.RETURN)
    except NoSuchElementException:
        print("Error: one or more message elements cannot be found.")
    except TimeoutException:
        print("Error: page [SEND_MESSAGE] timed out.")
    except:
        print("There was an error with the message you are trying to send. Please check its contents and try again.")

def test_lock():
    try:
        lock_button = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="celo-lock-button"]/div[1]')))
        lock_button.click()
    except NoSuchElementException:
        print("Error: lock button element cannot be found.")
    except TimeoutException:
        print("Error: page [LOCK] timed out.")
    except:
        print("Locking functionality failed. Please check and try again.")

def test_pin_reentry():
    pin = '5497'
    try:
        pin_area = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.XPATH, '//*[@id="pin_code_confirm"]')))
        pin_area.send_keys(pin)
    except NoSuchElementException:
        print("Error: pin area element cannot be found.")
    except TimeoutException:
        print("Error: page [PIN_REENTRY] timed out.")
    except:
        print("There was an error with your pin code. Please check it has been entered correctly and try again.")

def main():
    test_login()
    test_pin_codes_registration()
    test_send_message()
    test_lock()
    test_pin_reentry()


if __name__ == '__main__':
    main()





























