import tensorflow as tf
import numpy as np

from tensorflow.keras.layers import (Activation, AveragePooling2D, Flatten,
                                     BatchNormalization, Conv2D, Dense,
                                     Dropout, Input, MaxPooling2D)
from tensorflow.keras.models import Model

def mnist_cnn(input_shape,
          output_channels,
          activation="relu",
          dropout=0.4, pool_size=(2,2),
          filt_size=32,
          kernel_size=(3, 3)):

    inputs = Input(shape=input_shape)
    x = BatchNormalization()(inputs)

    """
    x = Conv2D(filt_size, kernel_size, padding="same", activation=activation, use_bias=False)(x)
    x = Dropout(dropout)(x)
    x = Conv2D(filt_size, kernel_size, padding="same", activation=activation, use_bias=False)(x)
    x = Dropout(dropout)(x)
    x = BatchNormalization()(x)
    """
    
    x = Conv2D(filt_size, kernel_size=(5, 5), activation=activation,
               strides=(2, 2), padding="same", use_bias=False)(x)
    x = Dropout(dropout)(x)
    x = BatchNormalization()(x)

    """
    x = Conv2D(64, kernel_size, padding="same", activation=activation, use_bias=False)(x)
    x = Dropout(dropout)(x)
    x = BatchNormalization()(x)
    x = Conv2D(64, kernel_size, padding="same", activation=activation, use_bias=False)(x)
    x = Dropout(dropout)(x)
    x = BatchNormalization()(x)
    """
    
    x = Conv2D(64, kernel_size=(5, 5), activation=activation,
               strides=(2, 2), padding="same", use_bias=False)(x)
    x = Dropout(dropout)(x)
    
    x = BatchNormalization()(x)
    x = Flatten()(x)
    x = Dense(128, activation=activation)(x)
    x = Dropout(dropout)(x)
    x = BatchNormalization()(x)
    x = Dense(output_channels, activation="softmax")(x)

    model = Model(inputs=[inputs], outputs=x)
    return model