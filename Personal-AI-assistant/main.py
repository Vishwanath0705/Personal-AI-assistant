import os
import eel
import webbrowser
import time

from engine.features import *

eel.init('www')

playAssistantSound()
eel.start('index.html', mode=None, host='127.0.0.1', port=5501, block=False)


webbrowser.get("firefox").open("http://127.0.0.1:5501/www/assests/index.html")

