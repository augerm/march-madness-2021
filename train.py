import tensorflow.keras as k
import numpy as np
from modules.matchups import Matchups

matchups = Matchups()

completed_matchups = matchups.get_completed_matchups()

train_x = list(map(lambda completed_matchup: completed_matchup.get_features(), completed_matchups))
train_y = list(map(lambda completed_matchup: completed_matchup.result, completed_matchups))

# Create neural network architecture
model = k.Sequential()
model.add(k.layers.Dense(len(train_x), input_dim=2, activation='relu'))
model.add(k.layers.Dense(8, activation='relu'))
model.add(k.layers.Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(np.array(train_x), np.array(train_y), epochs=1, batch_size=1000)

test_loss, test_acc = model.evaluate(np.array(train_x), np.array(train_y))

print('Test accuracy:', test_acc)