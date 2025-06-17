import cv2 as cv
import numpy as np
import time 

Video = cv.VideoCapture("volleyball_match.mp4")
time.sleep(2)

trail = []
max_trail = 5
while True:
    ret, frame = Video.read()
    if not ret:
        break

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    blur = cv.GaussianBlur(hsv, (11,11), 7)

    lower_yellow = np.array([40, 32, 138])
    upper_yellow = np.array([70, 245, 191])

    mask = cv.inRange(blur, lower_yellow, upper_yellow)

    contours, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        area = cv.contourArea(cnt)
        if 210 < area < 350:
        
            peri = cv.arcLength(cnt, closed=True)
            if peri > 0:
                cir = 4* (np.pi) * (area/ (peri)**2)
                if 0.65 < cir < 1.2:
                    (x, y), _= cv.minEnclosingCircle(cnt)
                    center = (int(x), int(y))
            

                    cv.circle(frame, center, 10, (0,255,0), 2)
        
                    trail.append(center)
                    if len(trail) > max_trail:
                        trail.pop(0)

    for i in range(1, len(trail)):
        if trail[i-1] is None or trail[i] is None:
            continue

        # thick = int(5 * (1 - i / max_trail)) + 1
        # color = (0, int(255 * (1 - i / max_trail)), 255)

        cv.line(frame, trail[i-1], trail[i], (0,0,255), 3)

    cv.imshow("Frame", frame)
    
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

Video.release()
cv.destroyAllWindows()
