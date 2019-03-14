import tensorflow.keras as k
from tensorflow.keras import metrics
import numpy as np
import datetime
from modules.matchups import Matchups
from modules.loss_function import get_loss_single


# maybe also load test data, and predict data!
def get_train_data():
    matchups = Matchups()
    completed_matchups = matchups.get_completed_matchups(until_year=2015)
    train_x = list(map(lambda completed_matchup: completed_matchup.get_features(), completed_matchups))
    train_y = list(map(lambda completed_matchup: completed_matchup.result, completed_matchups))
    train_x = train_x[:8000]
    train_y = train_y[:8000]
    print("finished loading train data")
    return np.array(train_x), np.array(train_y)


def train_model():
    train_x, train_y = get_train_data()
    # Create neural network architecture
    model = k.Sequential()
    model.add(k.layers.Dense(len(train_x), input_dim=len(train_x[0]), activation='sigmoid'))
    model.add(k.layers.Dense(600, activation='sigmoid'))
    model.add(k.layers.Dense(1, activation='sigmoid'))

    # optimizer - sgd, rmsprop
    model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=[metrics.binary_accuracy])
    model.fit(np.array(train_x), np.array(train_y), epochs=5, batch_size=32)

    test_loss, test_acc = model.evaluate(np.array(train_x), np.array(train_y))

    print('Test accuracy:', test_acc)

    date_str = str(datetime.datetime.now().strftime("%d-%B-%Y-%I-%M%p"))
    model.save('keras_models/{}.h5'.format(date_str))

train_model()