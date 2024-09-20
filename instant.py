import json
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
import time

# OPTIONS
url = 'https://instaling.pl/teacher.php?page=login'
login_set = "2p2259788"
password_set = "rxuxz"


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
driver = webdriver.Chrome(options=options)
action = ActionChains(driver)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
driver.get(url)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
time.sleep(5)
driver.find_element(By.CLASS_NAME, "fc-primary-button").click()
login = driver.find_element(By.ID, "log_email")
login.send_keys(login_set)
password = driver.find_element(By.ID, "log_password")
password.send_keys(password_set)
login_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
action.move_to_element(login_button).click().perform()
time.sleep(random.uniform(1.5, 3.0))
btn_sesion = driver.find_element(By.CLASS_NAME, "btn-session")
action.move_to_element(btn_sesion).click().perform()
time.sleep(random.uniform(1.5, 3.0))   
start_session_button = driver.find_element(By.ID, "start_session_button");
continue_session_button = driver.find_element(By.ID, "continue_session_button")

if start_session_button.size['width'] > 0 and start_session_button.size['height'] > 0:
    action.move_to_element(start_session_button).click().perform()
elif continue_session_button.size['width'] > 0 and continue_session_button.size['height'] > 0:
    action.move_to_element(continue_session_button).click().perform()


time.sleep(random.uniform(1.5, 3.0))
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
cos = True
with open('data.json', 'r') as file:
    data = json.load(file)

def input_answer(ans):
    driver.find_element(By.ID, "answer").send_keys(ans)
    time.sleep(random.uniform(1.5, 3.0))

while(cos):
    try:
        time.sleep(random.uniform(1.5, 3.0))
        given = driver.find_element(By.CLASS_NAME, "translations").text
        german_word = next((entry['german'] for entry in data if entry['polish'] == given), None)
        print(german_word)
        if(german_word != None):
            time.sleep(random.uniform(1.5, 3.0))
            input_answer(german_word)
            driver.find_element(By.ID, "check").click()
        else:
            new_word_var = driver.find_element(By.ID, "dont_know_new")
            if new_word_var.size['width'] > 0 and new_word_var.size['height'] > 0 and new_word_var:
                action.move_to_element(driver.find_element(By.ID, "dont_know_new")).click().perform()
                time.sleep(random.uniform(0.3, 1))
                action.move_to_element(driver.find_element(By.ID, "next_word")).click().perform()
                time.sleep(random.uniform(1.5, 3.0))
                continue;
            time.sleep(random.uniform(1.5, 3.0))
            action.move_to_element(driver.find_element(By.ID, "check")).click().perform()
            time.sleep(random.uniform(1.5, 3.0))
            correct = driver.find_element(By.ID, "word").text
            print(driver)
            new_entry = {"german": correct, "polish": given}
            data.append(new_entry)
            print("Updated data:", data)
            with open('data.json', 'w') as file:
                json.dump(data, file, indent=4)
        time.sleep(random.uniform(1.5, 3.0))
        action.move_to_element(driver.find_element(By.ID, "nextword")).click().perform()
    except NoSuchElementException:
        break

