import ctypes

import pyautogui


def mouse_to_primary_monitor(x, y):
    ctypes.windll.user32.SetCursorPos(x, y)
    ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)  # left down
    ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)  # left up
    pyautogui.leftClick(x=x - 50, y=y)