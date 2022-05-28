import numpy as np
import cv2
import dlib

clickar = 0
cap = cv2.VideoCapture("video.mp4")
detector = dlib.get_frontal_face_detector()

def mouse_click(event, x, y, flags, param):
    global clickar
    if event == cv2.EVENT_LBUTTONDOWN or event == cv2.EVENT_RBUTTONDOWN:
        clickar += 1
        print(clickar)
        if(clickar >= 4):
            clickar = 0
        pass

while True:
    print(clickar)
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
        try:
            if(clickar == 0):
               cv2.rectangle(frame, (x, y), (x1, y1), (0, 0, 255), 2)
            if(clickar == 2):
                frame[y:y1, x:x1] = cv2.blur(frame[y:y1, x:x1], (25, 25))
            if(clickar == 1):
                min_contrast = 5
                max_contrast = 200
                imgfb = cv2.GaussianBlur(frame,(5,5),0)
                frame = cv2.Canny(imgfb, min_contrast, max_contrast )
        except:
            pass
    cv2.imshow('video', frame)

    # Wait for key 'ESC' to quit
    key = cv2.waitKey(1) & 0xFF
    if key == 27:
        break
    cv2.setMouseCallback('video', mouse_click)

# That's how you exit
cap.release()
cv2.destroyAllWindows()
