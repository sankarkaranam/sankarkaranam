import cv2
import numpy as np
import os

face_cascade = cv2.CascadeClassifier('models/haarcascade_frontalface_default.xml')

def add_face(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

    for (x, y, w, h) in faces:
        face = gray[y:y+h, x:x+w]
        resized_face = cv2.resize(face, (100, 100))
        cv2.imwrite(image_path, resized_face)