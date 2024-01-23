import cv2
import numpy as np


def is_close(pt, points, min_dist):
    for point in points:
        if np.linalg.norm(np.array(pt) - np.array(point)) < min_dist:
            return True
    return False


class GemFinder:
    def __init__(self, min_distance, flawless_gem_filenames, perfect_gem_filenames):
        self.min_distance = min_distance
        self.found_gems = []
        self.flawless_gem_filenames = flawless_gem_filenames
        self.perfect_gem_filenames = perfect_gem_filenames
        self._allowed_gem_find_types = ['flawless', 'perfect', 'both']

    def inside_change_gem_find_type(self, gem_find_type):
        if gem_find_type not in self._allowed_gem_find_types:
            return

        self.found_gems.clear()
        if gem_find_type == 'flawless':
            self.add_flawless_gems()
        elif gem_find_type == 'perfect':
            self.add_perfect_gems()
        elif gem_find_type == 'both':
            self.add_flawless_gems()
            self.add_perfect_gems()

    def add_flawless_gems(self):
        for image_path in self.flawless_gem_filenames:
            read_image = cv2.imread(image_path, cv2.COLOR_RGB2BGR)
            self.found_gems.append(read_image)

    def add_perfect_gems(self):
        for image_path in self.perfect_gem_filenames:
            read_image = cv2.imread(image_path, cv2.COLOR_RGB2BGR)
            self.found_gems.append(read_image)

    def find_gems(self, screenshot):
        cv_screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
        gem_locations = []
        for image in self.found_gems:
            _, width, height = image.shape[::-1]
            result = cv2.matchTemplate(cv_screenshot, image, cv2.TM_CCOEFF_NORMED)
            threshold = 0.75
            locations = np.where(result >= threshold)

            for point in zip(*locations[::-1]):
                gem_locations.append([
                    point[0] + width / 2,
                    point[1] + height / 2
                ])

        unique_points = []
        for e in gem_locations:
            if not is_close(e, unique_points, self.min_distance):
                unique_points.append(e)

        gem_locations_sorted = sorted(unique_points, key=lambda p: (p[1], p[0]))
        return gem_locations_sorted
