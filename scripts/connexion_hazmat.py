from selenium.webdriver.support.ui import WebDriverWait, Select
import time
from config import settings
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def run_script(driver):

    actions = ActionChains(driver)

    # Access the page
    driver.get(settings.login_data["url"])
    time.sleep(2)

    # # Click "Save" Do not un coment this for now. Ask Zenha
    # driver.find_element(By.XPATH, "/html/body/form/div[3]/table/tbody/tr/td[2]/table/tbody/tr[2]/td[1]/div[3]/fieldset/input[1]").click()

    # Done
    print("✅ Upload done.")
    time.sleep(999999)