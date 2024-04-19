import cv2
import numpy as np

def detect_color(frame):

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
  
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])

    lower_green = np.array([40, 100, 100])
    upper_green = np.array([70, 255, 255])

    lower_blue = np.array([100, 100, 100])
    upper_blue = np.array([140, 200, 240])

    mask_red = cv2.inRange(hsv, lower_red, upper_red)
    mask_green = cv2.inRange(hsv, lower_green, upper_green)
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)


    area_red = cv2.countNonZero(mask_red)
    area_green = cv2.countNonZero(mask_green)
    area_blue = cv2.countNonZero(mask_blue)


    color = None
    if area_red > area_green and area_red > area_blue:
        color = "Rojo"
    elif area_green > area_red and area_green > area_blue:
        color = "Verde"
    elif area_blue > area_red and area_blue > area_green:
        color = "Azul"

    return color

# Inicializar la captura de video
cap = cv2.VideoCapture(1)

while True:

    ret, frame = cap.read()
    
 
    dominant_color = detect_color(frame)

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, dominant_color, (50, 50), font, 1, (125, 255, 255), 2, cv2.LINE_AA)
    

    cv2.imshow('Video en tiempo real', frame)
    

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()