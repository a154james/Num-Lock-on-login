from win32api import GetKeyState
from win32con import VK_NUMLOCK
import time
from pywinauto import keyboard
import ctypes

i = 1
while i = 1:
    keystate = GetKeyState(VK_NUMLOCK)
    if (keystate == 0):
        keyboard.send_keys("{NUMLOCK}", with_spaces=True)

    #GetKeyState(VK_NUMLOCK))
    #keyboard.send_keys("{NUMLOCK}", with_spaces=True)
    i += 1
    #print("run #: ", i)
    #time.sleep(1)