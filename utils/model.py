import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import toml


# initial_data_X = np.array(
#     [[1920, 1080], [1756, 1013], [1920, 1032], [1788, 1032], [1864, 965], [1904, 965], [1551, 965], [1797, 965],
#      [1300, 870], [1300, 763], [1332, 790], [1496, 877], [1548, 928], [1626, 969], [1507, 1028], [1623, 1028]])
# initial_data_y = np.array(
#     [[1280, 605], [1172, 574], [1326, 584], [1193, 583], [1308, 548], [1346, 547], [995, 548], [1242, 546], [799, 493],
#      [864, 435], [882, 447], [991, 498], [1014, 527], [1067, 549], [914, 582], [1028, 582]])
#
# poly_model.add_data(initial_data_X, initial_data_y)

class PolynomialRegressionModel:
    def __init__(self):
        self.poly = PolynomialFeatures(degree=2)
        self.model = LinearRegression()
        self.X = np.array([]).reshape(0, 2)
        self.y = np.array([]).reshape(0, 2)

    def add_data(self, x_new, y_new):
        """ 새로운 데이터를 추가합니다. """
        self.X = np.vstack([self.X, x_new])
        self.y = np.vstack([self.y, y_new])

    def train_model(self):
        """ 모델을 훈련합니다. """
        x_poly = self.poly.fit_transform(self.X)
        self.model.fit(x_poly, self.y)

    def predict(self, x_predict):
        """ 주어진 윈도우 크기에 대해 x, y축 값을 예측합니다. """
        x_predict_poly = self.poly.transform(x_predict)
        return self.model.predict(x_predict_poly)


class PolynomialRegressionModelTOML(PolynomialRegressionModel):
    def save_to_toml(self, file_path):
        """ 현재 데이터셋을 TOML 파일로 저장합니다. 보다 구조화된 형태로 저장합니다. """
        data = {'data': [{'window_size': list(map(int, X)), 'mouse_coords': list(map(int, y))}
                         for X, y in zip(self.X, self.y)]}
        with open(file_path, 'w') as file:
            toml.dump(data, file)

    def load_from_toml(self, file_path):
        """ TOML 파일로부터 데이터셋을 불러옵니다. 구조화된 형태의 데이터를 읽습니다. """
        with open(file_path, 'r') as file:
            data = toml.load(file)
        self.X = np.array([record['window_size'] for record in data['data']])
        self.y = np.array([record['mouse_coords'] for record in data['data']])
