import os # functions for interacting with the operating system
import cv2  #computer vision or load images & process images
import numpy as np  # arrays
import matplotlib.pyplot as plt  #visualisation of actual digits
import tensorflow as tf

mnist = tf.keras.datasets.mnist
# loading directly from tensorflow no need to dwnld
# splitting into testing data & training data
(x_train, y_train) , (x_test , y_test) = mnist.load_data()
# x = pixcel data  y = classification (no , digit)
# normalising or scaling it down
# 0-255(grayscale pixcel)
x_train  = tf.keras.utils.normalize(x_train, axis=1)
# normalising pixcels
x_test = tf.keras.utils.normalize(x_test, axis=1)





# model = tf.keras.models.Sequential()
# # adding layer and flattening into one big line of 784 pixcel
# model.add(tf.keras.layers.Flatten(input_shape=(28,28)))
# model.add(tf.keras.layers.Dense(128, activation='relu'))
# model.add(tf.keras.layers.Dense(128, activation='relu'))
# model.add(tf.keras.layers.Dense(10, activation='softmax'))
# # softmax - all neurons add up to 1
#
# # compiling model
# model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
#
# model.fit(x_train, y_train, epochs=5)
# model.save('hand.model')

model  = tf.keras.models.load_model('hand.model')

# loss, accuracy = model.evaluate(x_test, y_test)
# print(loss)
# print(accuracy)


image_number = 1
while os.path.isfile(f"Digits/{image_number}.png"):
    try:
        img = cv2.imread(f"Digits/}")
















