# SeleniumTest

Selenium を使ったブラウザ動作テストサンプルコード

## Usage

- 実行するとブラウザが起動し、テストが実行される

```bash
python run.py
```

- 結果データは `results/YYYYMMDD-HHMMSS` に保管される

## Requirements

- Python 3
- Browser Chrome or Edge
- Web Driver
  - Chrome Driver
    - https://googlechromelabs.github.io/chrome-for-testing/
  - Edge Driver
    - https://developer.microsoft.com/ja-jp/microsoft-edge/tools/webdriver

## Setup

- Python セットアップ

```bash
python -m venv .venv
./.venv/Scripts/Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

- WebDriver のダウンロードと配置

  - Chrome: `driver\chromedriver-win64\chromedriver.exe`
  - Edge: `driver\edgedriver-win32\msedgedriver.exe`

- `.env` の設定

```ini
SCREEN_SIZE_WIDTH=1080
SCREEN_SIZE_HEIGHT=800
CHROME_DRIVER=driver\chromedriver-win64\chromedriver.exe
EDGE_DRIVER=driver\edgedriver-win32\msedgedriver.exe
```
