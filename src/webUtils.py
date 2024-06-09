from src import config
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from enum import Enum
from selenium.webdriver.common.by import By
# 要素が特定条件を満たすまで待機
from selenium.webdriver.support.ui import WebDriverWait
# 要素が特定条件を満たすまで待機(WebDriverWait と組合せ)
from selenium.webdriver.support import expected_conditions as EC


class DRIVER_TYPE(Enum):
    """WebDriverの種類"""
    CHROME = 1
    EDGE = 2


def get_webdriver(driver_type: DRIVER_TYPE = DRIVER_TYPE.CHROME):
    """WebDriverの取得

    Args:
        driver_type (DRIVER_TYPE): chromeまたはedge。デフォルトは"chrome"。
    Returns:
        webdriver
    """
    if driver_type == DRIVER_TYPE.CHROME:
        return _get_chrome_driver()
    elif driver_type == DRIVER_TYPE.EDGE:
        return _get_edge_driver()


def save_screenshot(driver, file_name: str):
    """スクリーンショット取得

    Args:
        driver: webdriver
        file_name: ファイル名
    """
    driver.save_screenshot(os.path.join(
        config.result_folder_path, file_name + '.png'))


def save_html_soruce(driver, file_name: str):
    """ソース情報を保存

    Args:
        driver: webdriver
        file_name: ファイル名
    """
    html_source = driver.page_source
    with open(os.path.join(
            config.result_folder_path, file_name + '.txt'), 'w', encoding='utf-8') as file:
        file.write(html_source)


def wait_for_page_load(driver, timeout: float = 30):
    """ページロードが完了するまで待機

    Args:
        driver: webdriver
        timeout: タイムアウト時間(default: 30)
    """
    WebDriverWait(driver, timeout).until(
        lambda d: d.execute_script('return document.readyState') == 'complete'
    )


def wait_for_element(driver, css_selector: str, timeout: float = 30):
    """要素が見つかるまで待機

    Args:
        driver: webdriver
        css_selector: セレクタ指定の要素
        timeout: タイムアウト時間(default: 30)
    """
    WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, css_selector))
    )


_chrome_driver = None
_edge_driver = None


def _get_chrome_driver():
    global _chrome_driver
    if _chrome_driver is None:
        chrome_service = ChromeService(
            executable_path=config.chrome_driver_path)
        chrome_options = webdriver.ChromeOptions()
        _chrome_driver = webdriver.Chrome(
            options=chrome_options, service=chrome_service)
    return _chrome_driver


def _get_edge_driver():
    global _edge_driver
    if _edge_driver is None:
        edge_service = EdgeService(
            executable_path=config.edge_driver_path)
        edge_options = webdriver.EdgeOptions()
        _edge_driver = webdriver.Edge(
            options=edge_options, service=edge_service)
    return _edge_driver
