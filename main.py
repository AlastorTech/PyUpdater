from pyupdater.client import Client
from client_config import ClientConfig
import traceback
APP_NAME = "PyUpdater Tut"
APP_VERSION = "1.1.0"

ASSET_NAME = "ffmpeg"
ASSET_VERSION = '2.3.2'

def print_status_info(info):
    total = info.get(u'total')
    downloaded = info.get(u'downloaded')
    status = info.get(u'status')
    print (downloaded, total, status)

try:
    client = Client(ClientConfig())
    client.refresh()
except:
    traceback.print_exc()

client.add_progress_hook(print_status_info)
app_update = client.update_check(APP_NAME, APP_VERSION)
if app_update is not None:
    app_update.download()

    if app_update.is_downloaded():
        app_update.extract_restart()

try:
    with open('version.txt', 'w') as file:
        file.write(APP_VERSION)
        file.close()
except:
    print("PROBLEM")
    with open('version.txt', 'w') as file:
        text = f'{traceback.format_exc()}'
        file.write(APP_VERSION)
        file.close()
