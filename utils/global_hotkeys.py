from ctypes import windll
from ctypes import byref as ctypes_byref
from ctypes.wintypes import MSG as wintypes_MSG
from ctypes import windll, byref
from ctypes.wintypes import MSG
import threading
import win32con


class GlobalHotKeys(object):
    key_mapping = []
    user32 = windll.user32
    MOD_ALT = win32con.MOD_ALT
    MOD_CTRL = win32con.MOD_CONTROL
    MOD_CONTROL = win32con.MOD_CONTROL
    MOD_SHIFT = win32con.MOD_SHIFT
    MOD_WIN = win32con.MOD_WIN
    index = 0

    listen_thread = None
    listenning = False

    @classmethod
    def register(cls, vk, keyname, modifier=0, func=None):
        cls.key_mapping = [(vk_item, keyname_item, mod_item, func_item, index_item) for
                           vk_item, keyname_item, mod_item, func_item, index_item
                           in cls.key_mapping if vk_item != vk]
        cls.index += 1
        cls.key_mapping.append((vk, keyname, modifier, func, cls.index))

    @classmethod
    def unregister(cls, vk, mod_key=None):  # mod_key is now optional
        cls.key_mapping = [(vk_item, keyname_item, mod_item, func_item, index_item) for
                           vk_item, keyname_item, mod_item, func_item, index_item
                           in cls.key_mapping if vk_item != vk or (mod_key is not None and mod_key != mod_item)]
        for _, (vk_item, keyname, modifiers, func, index) in enumerate(cls.key_mapping):
            cls.user32.UnregisterHotKey(None, index)

    @classmethod
    def start_listen_thread(cls):
        cls.listen_thread = threading.Thread(target=cls.listen)
        cls.listen_thread.start()

    @classmethod
    def listen(cls):
        cls.listenning = True
        print(f"start listenning {cls.key_mapping}")
        for _, (vk, keyname, modifiers, func, index) in enumerate(cls.key_mapping):
            if not cls.user32.RegisterHotKey(None, index, modifiers, vk):
                input("Can't assign {} as hotkey. Press Enter to continue...".format(keyname[3:]))
                cls.stop()
                return

        msg = MSG()
        while cls.user32.GetMessageA(byref(msg), None, 0, 0) != 0:
            if msg.message == win32con.WM_HOTKEY:
                for _, (vk, keyname, modifiers, func, index) in enumerate(cls.key_mapping):
                    if msg.wParam == index:
                        if func:
                            func()

            cls.user32.TranslateMessage(byref(msg))
            cls.user32.DispatchMessageA(byref(msg))
            if not cls.listenning:
                break

    @classmethod
    def wait(cls):
        cls.listen_thread.join()

    @classmethod
    def stop(cls):
        print(f"cls.listenning: {cls.listen_thread.ident}")
        print(f"stop listenning {cls.key_mapping}")
        for i, (vk, keyname, modifiers, func, index) in enumerate(cls.key_mapping):
            print(f"unregister {vk} {keyname} {modifiers} {index}")
            cls.user32.UnregisterHotKey(None, index)
        del cls.key_mapping[:]
        cls.listenning = False

        cls.user32.PostThreadMessageA(cls.listen_thread.ident, win32con.WM_QUIT, 0, 0)

    @classmethod
    def _include_defined_vks(cls):
        for item in win32con.__dict__:
            item = str(item)
            if item[:3] == 'VK_':
                setattr(cls, item, win32con.__dict__[item])

    @classmethod
    def _include_alpha_vks(cls):
        for key_code in (range(ord('A'), ord('Z') + 1)):
            setattr(cls, 'VK_' + chr(key_code), key_code)

    @classmethod
    def _include_numeric_vks(cls):
        for key_code in (range(ord('0'), ord('9') + 1)):
            setattr(cls, 'VK_' + chr(key_code), key_code)


GlobalHotKeys._include_defined_vks()
GlobalHotKeys._include_alpha_vks()
GlobalHotKeys._include_numeric_vks()
