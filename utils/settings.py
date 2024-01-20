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
        self.window_title = 'Diablo II: Resurrected'

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
            'window_title': {
                'data': self.window_title,
                'description': '게임 창 제목'
            },
            'craft_button': {
                'data': self.craft_button,
                'description': '변환 버튼의 위치'
            },
        }
        with open('data.toml', 'w') as file:
            toml.dump(data, file)

    def load_from_toml(self):
        with open('data.toml', 'r') as file:
            data = toml.load(file)
        self.gem_min_distance = data['gem_min_distance']['data']
        self.gem_flawless_filenames = data['gem_flawless_filenames']['data']
        self.gem_perfect_filenames = data['gem_perfect_filenames']['data']
        self.window_title = data['window_title']['data']
        self.craft_button = data['craft_button']['data']