from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()

def closeTab():
    browser.close()

def switchTab():
    original_window = browser.current_window_handle
    for window_handle in browser.window_handles:
        if window_handle != original_window:
            browser.switch_to.window(window_handle)
            break