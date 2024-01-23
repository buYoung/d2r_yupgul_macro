import toml


class Settings:

    def __init__(self):
        self.gem_min_distance = 10
        self.gem_flawless_filenames = [
            'images/flawless_amethyst.png',
            'images/flawless_diamond.png',
            'images/flawless_emerald.png',
            'images/flawless_ruby.png',
            'images/flawless_sapphire.png',
            'images/flawless_topaz.png',
            'images/flawless_skull.png',
        ]
        self.gem_perfect_filenames = [
            'images/perfect_amethyst.png',
            'images/perfect_diamond.png',
            'images/perfect_emerald.png',
            'images/perfect_ruby.png',
            'images/perfect_sapphire.png',
            'images/perfect_topaz.png',
            'images/perfect_skull.png',
        ]
        self.gem_find_type = ''
        self.window_title = 'Diablo II: Resurrected'
        self.hot_key_gem_craft = ['Shift', 'W']

    def change_gem_find_type(self, gem_find_type):
        self.gem_find_type = gem_find_type
        self.save_to_toml()

    def change_gem_craft_hotkey(self, hot_key):
        self.hot_key_gem_craft = hot_key
        self.save_to_toml()

    def save_to_toml(self):
        data = {
            'gem_min_distance': {
                'data': self.gem_min_distance,
                'description': '보석인식시 보석 간 최소 거리'
            },
            'gem_flawless_filenames': {
                'data': self.gem_flawless_filenames,
                'description': '보석인식시 사용할 상급 보석 이미지 파일명'
            },
            'gem_perfect_filenames': {
                'data': self.gem_perfect_filenames,
                'description': '보석인식시 사용할 최상급 보석 이미지 파일명'
            },
            'gem_find_type': {
                'data': self.gem_find_type,
                'description': '보석인식시 사용할 보석 종류'
            },
            'window_title': {
                'data': self.window_title,
                'description': '게임 창 제목'
            },
            'hot_key_gem_craft': {
                'data': self.hot_key_gem_craft,
                'description': '보석함 조합 단축키'
            },
        }
        with open('settings.toml', 'w') as file:
            toml.dump(data, file)

    def load_from_toml(self):
        with open('settings.toml', 'r') as file:
            data = toml.load(file)
        self.gem_min_distance = data['gem_min_distance']['data']
        self.gem_flawless_filenames = data['gem_flawless_filenames']['data']
        self.gem_perfect_filenames = data['gem_perfect_filenames']['data']
        self.gem_find_type = data['gem_find_type']['data']
        self.window_title = data['window_title']['data']
        self.hot_key_gem_craft = data['hot_key_gem_craft']['data']
