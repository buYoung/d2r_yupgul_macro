import os
import sys

import pyautogui
import webview
import win32con

from utils.global_hotkeys import GlobalHotKeys


class WebGuiApi:
    def __init__(self, settings, gem_finder, find_and_craft_gems, exit_thread, global_hot_keys):
        self.find_and_craft_gems = find_and_craft_gems
        self.gem_finder = gem_finder
        self.settings = settings
        self.exit_thread = exit_thread
        self.global_hot_keys = global_hot_keys
        self.hot_keys = {
            'gem_craft': settings.hot_key_gem_craft,
            # 'jewel_reroll': settings.hot_key_jewel_reroll,
            # 'gem_box_extract': settings.hot_key_gem_box_extract
        }

    def get_default_hot_keys(self):
        return self.hot_keys

    def change_gem_find_type(self, gem_find_type):
        self.gem_finder.inside_change_gem_find_type(gem_find_type)
        self.settings.change_gem_find_type(gem_find_type)

    def set_hotKey(self, hot_key, mod_key, type):
        # type is gem_craft, jewel_reroll, gem_box_extract
        GlobalHotKeys.stop()
        GlobalHotKeys.wait()
        _mod_key = 0
        if mod_key == 'Ctrl':
            _mod_key = win32con.MOD_CONTROL
        elif mod_key == 'Alt':
            _mod_key = win32con.MOD_ALT
        elif mod_key == 'Shift':
            _mod_key = win32con.MOD_SHIFT
        if type == 'gem_craft':
            # if len(self.hot_keys['gem_craft']) == 1:
            #     vk_gem_craft_key_name = f"VK_{self.hot_keys['gem_craft'][0]}"
            #     vk_key = getattr(GlobalHotKeys, vk_gem_craft_key_name)
            # elif len(self.hot_keys['gem_craft']) == 2:
            #     vk_gem_craft_key_name = f"VK_{self.hot_keys['gem_craft'][1]}"
            #     vk_key = getattr(GlobalHotKeys, vk_gem_craft_key_name)
            #     vk_mod_key_name = f"MOD_{self.hot_keys['gem_craft'][0].upper()}"
            #     vk_mod_key = getattr(GlobalHotKeys, vk_mod_key_name)

            vk_key_name = f"VK_{hot_key}"
            vk_key = getattr(GlobalHotKeys, vk_key_name)
            GlobalHotKeys.register(vk_key, vk_key_name, _mod_key, self.find_and_craft_gems)
            pass

        elif type == 'jewel_reroll':
            pass
        elif type == 'gem_box_extract':
            pass

        exit_key_name = "VK_ESCAPE"
        exit_hotkey = getattr(GlobalHotKeys, f"{exit_key_name}")
        GlobalHotKeys.register(exit_hotkey, exit_key_name, GlobalHotKeys.MOD_SHIFT, self.exit_thread)
        GlobalHotKeys.start_listen_thread()
        self.settings.change_gem_craft_hotkey([mod_key, hot_key])
        print("change hotkey to type: {} {} + {}".format(type, mod_key, hot_key))


class WebGui:
    def __init__(self, web_gui_api):
        url = 'ui/dist/index.html'
        if getattr(sys, 'frozen', False):
            url = os.path.dirname(os.path.abspath(__file__)) + '/ui/dist/index.html'

        pyautogui.alert(url)
        self.window = webview.create_window(
            'D2 macro', url, width=800, height=600, js_api=web_gui_api
        )
        self.window.events.closing += self.on_closing
        self.window.events.closed += self.on_closed

    def serve(self):
        webview.start(debug=False)

    def close(self):
        self.window.destroy()

    def on_closing(self):
        GlobalHotKeys.stop()

    def on_closed(self):
        exit(0)