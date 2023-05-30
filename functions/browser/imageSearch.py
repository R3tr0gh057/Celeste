import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def imgsearch(query):
    search_element = '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea'
    button_element = '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/button'
    opt = webdriver.ChromeOptions()
    opt.add_argument("--disable-popup-blocking")
    opt.add_argument("--disable-extentions")
    opt.add_experimental_option("detach", True)
    browser = webdriver.Chrome(chrome_options=opt)
    wait = WebDriverWait(browser, 10)

    try:
        browser.get('https://images.google.com/')
        wait.until(EC.presence_of_all_elements_located((By.XPATH, button_element)))
        selector = browser.find_element(By.XPATH, search_element)
        enter = browser.find_element(By.XPATH, button_element)

        selector.send_keys(query)
        enter.click()

    except selenium.common.exceptions.NoSuchElementException:
        print('Missing element')
    
    except selenium.common.exceptions.ElementNotInteractableException:
        print('Element not interactable')