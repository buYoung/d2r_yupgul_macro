import os

import numpy as np
import pyautogui
import pygetwindow as gw
import webview
from PIL import ImageGrab

from features.gem_craft.find_gem import GemFinder
from features.gui.web_gui import WebGui, WebGuiApi
from utils.global_hotkeys import GlobalHotKeys
from utils.macros import mouse_to_primary_monitor
from utils.model import PolynomialRegressionModelTOML
from utils.settings import Settings
from threading import Thread


def initialize(poly_model):
    poly_model.load_from_toml('data.toml')
    poly_model.train_model()


def diablo2_window_size():
    diablo2_window = gw.getWindowsWithTitle('Diablo II: Resurrected')[0]
    return (diablo2_window.left, diablo2_window.top,
            diablo2_window.width, diablo2_window.height)


def get_craft_button_location():
    _craft_button_x, _craft_button_y = _poly_model.predict(np.array([[width, height]]))[0]
    return int(_craft_button_x + left), int(_craft_button_y + top)


def find_and_craft_gems():
    print('find_and_craft_gems')
    if len(gem_finder.found_gems) == 0:
        pyautogui.alert('보석인식시 사용할 보석 종류를 선택해주세요.')
        return

    screen_shot = ImageGrab.grab(bbox=(left, top, left + width, top + height))
    screen_shot.save('screenshot.png')
    locations = gem_finder.find_gems(screen_shot)

    for location in locations:
        pyautogui.keyDown('ctrl')
        pyautogui.click(x=location[0] + left, y=location[1] + top)
        pyautogui.keyUp('ctrl')
        pyautogui.leftClick(x=craft_button_x, y=craft_button_y)


def exit_thread():
    gui.close()
    exit(0)


def init_hotkey():
    exit_key_name = "VK_ESCAPE"
    exit_hotkey = getattr(GlobalHotKeys, f"{exit_key_name}")

    gem_craft_hotkey = settings.hot_key_gem_craft
    if len(gem_craft_hotkey) == 1:
        vk_gem_craft_key_name = f"VK_{gem_craft_hotkey[0]}"
        vk_key = getattr(GlobalHotKeys, vk_gem_craft_key_name)
        GlobalHotKeys.register(vk_key, vk_gem_craft_key_name, GlobalHotKeys.MOD_SHIFT, find_and_craft_gems)
    elif len(gem_craft_hotkey) == 2:
        vk_gem_craft_key_name = f"VK_{gem_craft_hotkey[1]}"
        vk_key = getattr(GlobalHotKeys, vk_gem_craft_key_name)
        vk_mod_key_name = f"MOD_{gem_craft_hotkey[0].upper()}"
        vk_mod_key = getattr(GlobalHotKeys, vk_mod_key_name)
        GlobalHotKeys.register(vk_key, vk_gem_craft_key_name, vk_mod_key, find_and_craft_gems)
    GlobalHotKeys.register(exit_hotkey, exit_key_name, GlobalHotKeys.MOD_SHIFT, exit_thread)


if __name__ == '__main__':
    settings = Settings()
    if os.path.isfile('settings.toml'):
        settings.load_from_toml()
    else:
        settings.save_to_toml()

    gem_finder = GemFinder(settings.gem_min_distance, settings.gem_flawless_filenames, settings.gem_perfect_filenames)

    _poly_model = PolynomialRegressionModelTOML()
    initialize(_poly_model)
    left, top, width, height = diablo2_window_size()
    craft_button_x, craft_button_y = get_craft_button_location()
    craft_button_x = int(craft_button_x)
    craft_button_y = int(craft_button_y)
    mouse_to_primary_monitor(craft_button_x, craft_button_y)

    init_hotkey()
    # def find_and_craft_gems():
    GlobalHotKeys.start_listen_thread()

    web_gui_api = WebGuiApi(
        settings=settings,
        gem_finder=gem_finder,
        find_and_craft_gems=find_and_craft_gems,
        exit_thread=exit_thread,
        global_hot_keys=GlobalHotKeys
    )
    gui = WebGui(web_gui_api)
    gui.serve()
