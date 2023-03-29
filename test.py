from percy import percy_snapshot
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.bt.com/products/broadband/gaming')
browser.implicitly_wait(10)

percy_snapshot(browser, 'BT - Products - Gaming')
