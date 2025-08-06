from pynput.keyboard import Key, Controller
import time

Keyboard = Controller()

time.sleep(5)
for i in 10:
     for letter in "Hola puta :3":
		Keyboard.press(letter)
		Keyboard.release(letter)
	Keyboard.press(Key.enter)
