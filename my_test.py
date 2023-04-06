import sys
import random

from helper_class import Utilities
from percy import percy_snapshot
from selenium import webdriver

utils = Utilities()
percy_token = "percy_token"
unique_id = random.randint(1000000, 9999999)


def run_test():
    browser = webdriver.Chrome()
    browser.get('https://www.bt.com/products/broadband/gaming')
    browser.implicitly_wait(10)

    percy_snapshot(browser, 'BT - Products - Gaming')


def run_test_via_percy():
    utils.run_through_percy(percy_token, sys.argv[0], run_test.__name__, str(unique_id))


if __name__ == '__main__':
    globals()[sys.argv[1]]()
