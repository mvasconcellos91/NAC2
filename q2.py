#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import cv2
import dlib

# caso não tenha webcam escolha um video de teste .mp4.
cap = cv2.VideoCapture("video.mp4")
detector = dlib.get_frontal_face_detector()


while True:
    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    filtroSobreposicao = cv2.imread("img/rainbow.png",-1)
    face = detector(gray, 0)
    boca_pontos = list(range(61, 68))  
    

    for i in face:
        x = i.left()
        y = i.top()
        x1 = i.right()
        y1 = i.bottom()

    videoNormal = cv2.rectangle(frame, (x, y), (x1, y1), (0, 0, 255), 2)
    cv2.imshow("Normal", videoNormal)
    videoDesfocado = frame[y:y1, x:x1] = cv2.blur(frame[y:y1, x:x1], (25, 25))
    cv2.imshow("Desfocado", videoDesfocado)
    min_contrast = 5
    max_contrast = 200
    imgfb = cv2.GaussianBlur(frame,(5,5),0)
    videoCanny = cv2.Canny(imgfb, min_contrast, max_contrast )
    cv2.imshow("Canny", videoCanny)

    

    # Wait for key 'ESC' to quit
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break

# That's how you exit
cap.release()
cv2.destroyAllWindows()
