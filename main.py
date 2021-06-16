import time
from datetime import datetime
from pynput.keyboard import Controller, Key
from data import lst
import webbrowser

keyboard = Controller()

isStarted = False

for i in lst:
    while True:
        if not isStarted:
            if datetime.now().hour == int(i[1].split(':')[0]) and datetime.now().minute == int(i[1].split(':')[1]):
                webbrowser.open(i[0])
                isStarted = True
        else:
            if datetime.now().hour == int(i[2].split(':')[0]) and datetime.now().minute == int(i[2].split(':')[1]):
                keyboard.press('w')
                time.sleep(1)
                keyboard.press(Key.enter)
                isStarted = False
                break
        time.sleep(5)
