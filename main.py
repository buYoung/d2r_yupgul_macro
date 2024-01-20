import numpy as np
import pyautogui
import pygetwindow as gw
from PIL import ImageGrab

from features.gem_craft.find_gem import GemFinder
from utils.global_hotkeys import GlobalHotKeys
from utils.macros import mouse_to_primary_monitor
from utils.model import PolynomialRegressionModelTOML
from utils.settings import Settings


def initialize(poly_model):
    poly_model.load_from_toml('data.toml')
    poly_model.train_model()


def diablo2_window_size():
    diablo2_window = gw.getWindowsWithTitle('Diablo II: Resurrected')[0]
    return (diablo2_window.left, diablo2_window.top,
            diablo2_window.width, diablo2_window.height)


def capture_gems(settings):
    screen_shot = ImageGrab.grab(bbox=(left, top, left + width, top + height))
    screen_shot.save('screenshot.png')

    gem_finder = GemFinder(settings.gem_min_distance, settings.gem_flawless_filenames, settings.gem_perfect_filenames)
    # gem_finder.add_flawless_gems()
    gem_finder.add_perfect_gems()

    gem_locations = gem_finder.find_gems(screen_shot)

    return gem_locations


def get_craft_button_location():
    _craft_button_x, _craft_button_y = _poly_model.predict(np.array([[width, height]]))[0]
    return int(_craft_button_x + left), int(_craft_button_y + top)


@GlobalHotKeys.register(GlobalHotKeys.VK_W, "VK_W", GlobalHotKeys.MOD_SHIFT)
def find_and_craft_gems():
    locations = capture_gems(settings)

    for location in locations:
        pyautogui.keyDown('ctrl')
        pyautogui.click(x=location[0] + left, y=location[1] + top)
        pyautogui.keyUp('ctrl')
        pyautogui.leftClick(x=craft_button_x, y=craft_button_y)


if __name__ == '__main__':
    settings = Settings()
    _poly_model = PolynomialRegressionModelTOML()
    initialize(_poly_model)
    left, top, width, height = diablo2_window_size()
    craft_button_x, craft_button_y = get_craft_button_location()
    craft_button_x = int(craft_button_x)
    craft_button_y = int(craft_button_y)
    mouse_to_primary_monitor(craft_button_x, craft_button_y)

    GlobalHotKeys.register(GlobalHotKeys.VK_ESCAPE, "VK_ESCAPE", GlobalHotKeys.MOD_SHIFT, False)

    GlobalHotKeys.listen()
