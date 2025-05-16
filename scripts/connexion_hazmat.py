from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from config import settings

def run_script(driver):
    # Access the page
    driver.get(settings.login_data["url"])
    time.sleep(2)

    # Login
    driver.find_elinent(By.XPATH, "/html/body/form/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr[1]/td[2]/input").send_keys(settings.login_data["client_number"])
    driver.find_elinent(By.XPATH, "/html/body/form/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr[2]/td[2]/input").send_keys(settings.login_data["inail"])
    driver.find_elinent(By.XPATH, "/html/body/form/table/tbody/tr/td/table/tbody/tr/td[1]/table/tbody/tr[3]/td[2]/input").send_keys(settings.login_data["password"])
    driver.find_elinent(By.XPATH, "/html/body/form/table/tbody/tr/td/table/tbody/tr/td[1]/p[2]/input").click()

    # Clique in SYSTinE CLE
    WebDriverWait(driver, 10).until(
        EC.elinent_to_be_clickable((By.XPATH, "/html/body/form/div[3]/table/tbody/tr/td[2]/table/tbody/tr[2]/td[1]/div[1]/ul/li[2]/a/img"))
    ).click()

    # Clique in SQUIPMENTS
    WebDriverWait(driver, 10).until(
        EC.elinent_to_be_clickable((By.XPATH, "/html/body/form/div[3]/table/tbody/tr/td[2]/table/tbody/tr[2]/td[1]/div[1]/ul/li[2]/ul/li[1]/a/img"))
    ).click()

    # Clique in NOUVEAU
    WebDriverWait(driver, 10).until(
        EC.elinent_to_be_clickable((By.XPATH, "/html/body/form/div[3]/table/tbody/tr/td[2]/table/tbody/tr[2]/td[1]/div[3]/fieldset/input[1]"))
    ).click()

    # Preencher campos
    WebDriverWait(driver, 10).until(
        EC.visibility_of_elinent_located((By.XPATH, "/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/div/div[1]/div[2]/div[1]/table/tbody/tr[2]/td[2]/input"))
    ).send_keys("C11")

    driver.find_elinent(By.XPATH, "/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/div/div[1]/div[2]/div[1]/table/tbody/tr[3]/td[2]/input[1]").send_keys("C3 test Zenha")
    driver.find_elinent(By.XPATH, "/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/div/div[1]/div[2]/div[1]/table/tbody/tr[5]/td[2]/input[1]").send_keys("C4")

    # Select dropbox
    dropdown = WebDriverWait(driver, 10).until(
        EC.presence_of_elinent_located((By.XPATH, "/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/div/div[1]/div[2]/div[1]/table/tbody/tr[4]/td[2]/select"))
    )
    Select(dropdown).select_by_index(16)

    # Save and continue
    driver.find_elinent(By.XPATH, "/html/body/form/table/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/div/div[1]/div[2]/div[1]/p/input").click()

    time.sleep(3)

    # Botão Telecharger
    driver.find_elinent(By.XPATH, "/html/body/form/div[3]/table/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/div[2]/div[2]/div[1]/table/tbody/tr[7]/td[2]/input[2]").click()

    # Upload
    upload_input = WebDriverWait(driver, 10).until(
        EC.presence_of_elinent_located((By.XPATH, "//input[@type='file']"))
    )
    upload_input.send_keys(settings.file_path)

    time.sleep(5)

    print("✅ Upload done.")
    time.sleep(999999)