import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def gogsearch(query):
    search_element = '#APjFqb' #search abr css selector
    button_element = 'gNO89b' #search button class name
    opt = webdriver.ChromeOptions()
    opt.add_argument("--disable-popup-blocking")
    opt.add_argument("--disable-extentions")
    opt.add_experimental_option("detach", True)
    browser = webdriver.Chrome(chrome_options=opt)
    wait = WebDriverWait(browser, 10)

    try:
        browser.get('https://www.google.com/')
        wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, button_element)))
        selector = browser.find_element(By.CSS_SELECTOR, search_element)
        enter = browser.find_element(By.CLASS_NAME, button_element)
        selector.send_keys(query)
        enter.click()

    except selenium.common.exceptions.NoSuchElementException:
        print('Missing element')
    
    except selenium.common.exceptions.ElementNotInteractableException:
        print('Element not interactable')