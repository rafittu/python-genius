import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.optimizers import Adam
from database.models.color import Color

def create_model(input_shape):
    model = Sequential()
    model.add(LSTM(50, activation='relu', input_shape=input_shape))
    model.add(Dense(3, activation='sigmoid'))
    model.compile(optimizer=Adam(learning_rate=0.001), loss='mse')
    return model


model = create_model((None, 3))


def get_last_n_colors(n):
    colors = Color.query.order_by(Color.timestamp.desc()).limit(n).all()
    colors.reverse()
    data = np.array([[c.red, c.green, c.blue] for c in colors]) / 255.0
    return data


def train_model(n):
    data = get_last_n_colors(n)
    if len(data) > 1:
        X, y = data[:-1], data[1:]
        X = X.reshape((1, X.shape[0], X.shape[1]))
        y = y.reshape((1, y.shape[0], y.shape[1]))
        model.fit(X, y, epochs=1, verbose=0)
