from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_raw():

    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    wait = WebDriverWait(driver, 10)

    driver.get("https://www.saucedemo.com/")

    username = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "user-name")
        )
    )

    username.send_keys("standard_user")

    password = driver.find_element(
        By.ID,
        "password"
    )

    password.send_keys("secret_sauce")

    login_button = driver.find_element(
        By.ID,
        "login-button"
    )

    login_button.click()

    wait.until(
        EC.url_contains("inventory")
    )

    assert "inventory" in driver.current_url

    driver.quit()