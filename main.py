from selenium import webdriver
from scrapper import run_test

if __name__ == "__main__":
    driver = webdriver.Chrome()
    run_test(driver)