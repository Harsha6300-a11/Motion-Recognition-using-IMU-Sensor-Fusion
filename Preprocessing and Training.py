import os
import numpy as np
import tensorflow as tf
from sklearn . model_selection import train_test_split
# Load data
data = []
labels = []
label_map = {" move_none ": 0, " move_circle ": 1, " move_shake ": 2, " move_twist ": 3}
for label_name in os. listdir (" motion_data "):
    for file in os. listdir (f" motion_data /{ label_name }"):
        if file . endswith (". npy"):
            sample = np. load (f" motion_data /{ label_name }/{ file }")
            sample = sample . flatten () # Shape : (300 ,)
            data . append ( sample )
            labels . append ( label_map [ label_name ])
X = np. array ( data )
y = tf. keras . utils . to_categorical (labels , num_classes =4)
X_train , X_val , y_train , y_val = train_test_split (X, y, test_size =0.2 , random_state=42)
# Fully connected model
model = tf. keras . Sequential ([
    tf. keras . layers . Input ( shape =(300 ,) ),
    tf. keras . layers . Dense (128 , activation =’relu ’),
    tf. keras . layers . Dense (64 , activation =’relu ’),
    tf. keras . layers . Dense (4, activation =’softmax ’)
])
model . compile ( optimizer =’adam ’,
    loss =’ categorical_crossentropy ’,
    metrics =[ ’accuracy ’])
model .fit( X_train , y_train , validation_data =( X_val , y_val ), batch_size =1, epochs =15)
