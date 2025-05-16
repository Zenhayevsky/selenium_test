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

    # Login
    driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr[1]/td[2]/input").send_keys(settings.login_data["client_number"])
    driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr[2]/td[2]/input").send_keys(settings.login_data["email"])
    driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr[3]/td[2]/input").send_keys(settings.login_data["password"])
    driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr/td/table/tbody/tr/td[1]/p[2]/input").click()

    # Locate the "SYSTEME CLE" button
    systeme_cle = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/form/div[3]/table/tbody/tr/td[2]/table/tbody/tr[2]/td[1]/div[1]/ul/li[2]/a/img"))
    )

    # Hover over it to reveal the floating submenu
    actions.move_to_element(systeme_cle).perform()

    # Wait for the floating "SQUIPMENTS" button to become clickable
    squipments = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,
                                    "/html/body/form/div[3]/table/tbody/tr/td[2]/table/tbody/tr[2]/td[1]/div[1]/ul/li[2]/ul/li[1]/a/img"))
    )

    # Click the "SQUIPMENTS" button
    squipments.click()

    # Click "NOUVEAU"
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/form/div[3]/table/tbody/tr/td[2]/table/tbody/tr[2]/td[1]/div[3]/fieldset/input[1]"))
    ).click()

    # Fill in the fields
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/div/div[1]/div[2]/div[1]/table/tbody/tr[2]/td[2]/input"))
    ).send_keys("C12")

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/div/div[1]/div[2]/div[1]/table/tbody/tr[3]/td[2]/input[1]"))
    ).send_keys("C3 test Zenha")

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/div/div[1]/div[2]/div[1]/table/tbody/tr[5]/td[2]/input[1]"))
    ).send_keys("C4")

    # Dropdown - select the 17th option
    dropdown_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/div/div[1]/div[2]/div[1]/table/tbody/tr[4]/td[2]/select"))
    )
    select = Select(dropdown_element)
    select.select_by_index(16)

    # Click the "Save and Continue" button
    driver.find_element(By.XPATH, "/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/div/div[1]/div[2]/div[1]/p/input").click()

    # Wait 3 seconds after upload
    time.sleep(3)

    # Click the "Télécharger" button
    driver.find_element(By.XPATH, "/html/body/form/div[3]/table/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/div[2]/div[2]/div[1]/table/tbody/tr[7]/td[2]/input[2]").click()

    # Upload file (directly send path to input[type=file])
    upload_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='file']"))
    )
    upload_input.send_keys(settings.file_path)  # Send the file path directly

    # Wait 5 seconds after upload
    time.sleep(5)

    # # Click "Save"
    # driver.find_element(By.XPATH, "/html/body/form/div[3]/table/tbody/tr/td[2]/table/tbody/tr[2]/td[1]/div[3]/fieldset/input[1]").click()

    # Done
    print("✅ Upload done.")
    time.sleep(999999)