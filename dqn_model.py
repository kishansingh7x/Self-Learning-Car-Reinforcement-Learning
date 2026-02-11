from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Input
from tensorflow.keras.optimizers import Adam

def build_model(state_size, action_size):
    model = Sequential([
        Input(shape=(state_size,)),
        Dense(24, activation='relu'),
        Dense(24, activation='relu'),
        Dense(action_size, activation='linear')
    ])

    model.compile(
        optimizer=Adam(learning_rate=0.001),
        loss='mse'
    )
    return model
