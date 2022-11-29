import os

try:
	import eel, playsound.playsound
except ImportError:
	os.system('pip install eel playsound')



eel.init('./pub/')

@eel.expose
def screamer_playsound():
	playsound()

eel.start('index.htm', mode="chrome", size=(960, 960))
