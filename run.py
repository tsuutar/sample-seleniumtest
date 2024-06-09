from src import config, webUtils
import os
import time
import csv
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
# 要素が特定条件を満たすまで待機
from selenium.webdriver.support.ui import WebDriverWait
# 要素が特定条件を満たすまで待機(WebDriverWait と組合せ)
from selenium.webdriver.support import expected_conditions as EC

if __name__ == "__main__":
    driver = None
    try:
        driver = webUtils.get_webdriver(webUtils.DRIVER_TYPE.CHROME)
        driver.set_window_size(config.screen_size_width,
                               config.screen_size_heigth)
        driver.set_window_position(0, 0)
        # タイムアウトを10秒に設定
        wait = WebDriverWait(driver, 10)

        # テスト開始
        driver.get('https://www.google.co.jp/')
        webUtils.wait_for_page_load(driver)

        print(driver.current_url)
        webUtils.save_screenshot(driver, 'page-01')
        webUtils.save_html_soruce(driver, 'page-01')
        time.sleep(1)

        search_box = driver.find_element(By.CSS_SELECTOR, "[name=q]")
        search_box.send_keys('ChromeDriver')
        search_box.submit()
        webUtils.wait_for_element(driver, "div#search")

        webUtils.save_screenshot(driver, 'page-02')
        webUtils.save_html_soruce(driver, 'page-02')
    except Exception as e:
        print(e)
    finally:
        # WebDriverの終了
        if driver != None:
            driver.quit()

    print('quit')
