import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def ytsearch(query):
    search_element = '/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/form/div[1]/div[1]/input' #search abr css selector
    button_element = '/html/body/ytd-app/div[1]/div/ytd-masthead/div[4]/div[2]/ytd-searchbox/button' #search button class name
    video_element = '/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[1]/div[1]/div/div[1]/div/h3/a/yt-formatted-string'
    opt = webdriver.ChromeOptions()
    opt.add_argument("--disable-popup-blocking")
    opt.add_argument("--disable-extentions")
    opt.add_experimental_option("detach", True)
    browser = webdriver.Chrome(chrome_options=opt)
    wait = WebDriverWait(browser, 10)

    try:
        browser.get('https://www.youtube.com/')
        wait.until(EC.presence_of_element_located((By.XPATH, button_element)))
        selector = browser.find_element(By.XPATH, search_element)
        enter = browser.find_element(By.XPATH, button_element)
        selector.send_keys(query)
        enter.click()

        wait.until(EC.presence_of_element_located((By.XPATH, video_element)))
        vid_click = browser.find_element(By.XPATH, video_element)
        vid_click.click()

    except selenium.common.exceptions.NoSuchElementException:
        print('Missing element')
    
    except selenium.common.exceptions.ElementNotInteractableException:
        print('Element not interactable')