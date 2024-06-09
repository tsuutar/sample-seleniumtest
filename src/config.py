from dotenv import load_dotenv
import os
from datetime import datetime

# .envファイルのパスを指定して読み込む
load_dotenv()

# 現在の日付と時刻を取得
current_datetime = datetime.now()

# 設定取得
screen_size_width = os.getenv('SCREEN_SIZE_WIDTH', '1024')
screen_size_heigth = os.getenv('SCREEN_SIZE_HEIGHT', '768')
chrome_driver_path = os.getenv(
    'CHROME_DRIVER', 'driver\chromedriver-win64\chromedriver.exe')
edge_driver_path = os.getenv(
    'EDGE_DRIVER', 'driver\edgedriver-win32\msedgedriver.exe')

# 結果保存先の作成
result_folder_path = os.path.join(
    'results', current_datetime.strftime('%Y%m%d-%H%M%S'))
if not os.path.exists(result_folder_path):
    os.makedirs(result_folder_path)
