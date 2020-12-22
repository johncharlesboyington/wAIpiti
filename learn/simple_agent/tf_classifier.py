import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential


def train_tf_classifier():
    """Docstring."""

    # import and parse the data
    with open('state_action_pairs.txt', 'r') as F:
        lines = F.readlines()
    data = []
    labels = []
    for line in lines:
        line = line.split()
        data.append([int(line[1][1]), int(line[2][0])])
        labels.append(int(line[0]))
    
    # create a model
    model = tf.keras.models.Sequential([
      tf.keras.layers.Flatten(input_shape=(2,)),
      tf.keras.layers.Dense(4, activation='sigmoid'),
      tf.keras.layers.Dense(1, activation='sigmoid'),
    ])
    
    # compile the model
    model.compile(optimizer='adam',
                  loss=tf.keras.losses.BinaryCrossentropy(),
                  metrics=['accuracy'])
    
    # train the model
    model.fit(data, labels, epochs=20)
    
    # make a prediction
    prediction = model.predict([(0, 0), (0, 1), (1, 0), (1, 1)])
    print(prediction)
    return


if __name__ == '__main__':
    train_tf_classifier()
