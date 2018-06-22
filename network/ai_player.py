from keras.models import load_model
import selenium
from mss import mss
import cv2
import numpy as np 
import time
import os
model = load_model(os.path.join('network','dino_ai_weights_post_train.h5'))
start = time.time()

def predict(game_element):
    sct = mss()
    coordinates = {
        'top': 300,
        'left': 290,
        'width': 450,
        'height': 160,
    }

    img = np.array(sct.grab(coordinates))

    img = img[::,75:615]
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.Canny(img, threshold1=100, threshold2=200)
    img =cv2.resize(img, (0,0), fx=0.5, fy=0.5)
    img = img[None, :,:, None]
    img = np.array(img)

    y_prob = model.predict(img)
    print(y_prob)
    prediction = y_prob.argmax(axis=-1)
    if prediction == 1:
        print('JUMP')
        time.sleep(0.07)
        game_element.send_keys(u'\ue013')
    if prediction == 0:
        print("DO nothing")
        pass
    if prediction == 2:
        print('DUCK')
        game_element.send_keys(u'\ue015')		