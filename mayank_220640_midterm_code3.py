import cv2
import numpy as np
def colour(s):
    image = cv2.imread(s)
    image=cv2.resize(image,(500,500))
    cv2.imshow("original image",image)

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    mask = cv2.inRange(hsv, lower_red, upper_red)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    cv2.drawContours(image, contours, -1, (255, 0, 0), 2)
    return image
path=r"C:\Users\mayan\OneDrive\Desktop\cv drone\gem3.png"
cv2.imshow('Contours around Red Objects', colour(path))
cv2.waitKey(0)
cv2.destroyAllWindows()
