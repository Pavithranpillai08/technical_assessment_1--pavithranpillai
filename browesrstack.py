from selenium import webdriver
from scrapper import run_test
import os
from dotenv import load_dotenv
import threading

load_dotenv()

USERNAME = os.getenv("BROWSERSTACK_USERNAME")
ACCESS_KEY = os.getenv("BROWSERSTACK_ACCESS_KEY")


def create_browserstack_driver(os_name, os_version, browser_name, browser_version):

    options = webdriver.ChromeOptions()

    options.set_capability("browserName", browser_name)
    options.set_capability("browserVersion", browser_version)

    options.set_capability("bstack:options", {
        "os": os_name,
        "osVersion": os_version,
        "userName": USERNAME,
        "accessKey": ACCESS_KEY,
        "sessionName": "ElPais Scraper Test"
    })

    return webdriver.Remote(
        command_executor="https://hub-cloud.browserstack.com/wd/hub",
        options=options
    )


if __name__ == "__main__":

    # here is the version of browsers
    browsers = [
        ("Windows", "10", "Chrome", "latest"),
        ("Windows", "11", "Edge", "latest"),
        ("OS X", "Ventura", "Safari", "latest"),
        ("OS X", "Monterey", "Firefox", "latest"),
        ("Windows", "10", "Firefox", "latest")
    ]

    threads = []

    def thread_runner(browser):
        driver = create_browserstack_driver(*browser)
        run_test(driver)
        driver.quit()

    for browser in browsers:
        t = threading.Thread(target=thread_runner, args=(browser,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()