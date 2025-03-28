import time
import keyboard
x = 1
while x < 1000000:
    keyboard.press("a")
    x =+ 1
    time.sleep(0.01)
