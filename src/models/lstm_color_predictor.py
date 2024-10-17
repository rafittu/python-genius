from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.optimizers import Adam

def create_model(input_shape):
    model = Sequential()
    model.add(LSTM(50, activation='relu', input_shape=input_shape))
    model.add(Dense(3, activation='sigmoid'))
    model.compile(optimizer=Adam(learning_rate=0.001), loss='mse')
    return model


model = create_model((None, 3))
