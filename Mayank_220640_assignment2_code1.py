import cv2
import numpy as np
def generate():
    flag = np.ones((600, 600, 3), dtype=np.uint8) * 255
    cv2.rectangle(flag, (0, 0), (600, 200), (0, 153, 255), -1)
    cv2.rectangle(flag, (0, 200), (600, 400), (255, 255, 255), -1)
    cv2.rectangle(flag, (0, 400), (600, 600), (0, 120, 0), -1)

    center = (300, 300)
    radius = 100
    cv2.circle(flag, center, radius, (255, 0, 0), 2)
    num_spokes = 24  # You can change this number
    loop=int(num_spokes/2)
    
    for i in range(loop):
        angle = (360 / num_spokes) * i
        x1 = int(center[0] + radius * np.cos(np.radians(angle)))
        y1 = int(center[1] + radius * np.sin(np.radians(angle)))
        x2 = int(center[0] + radius * np.cos(np.radians(angle+180)))
        y2 = int(center[1] + radius * np.sin(np.radians(angle+180)))
        cv2.line(flag, (x1, y1), (x2, y2), (255,0,0), 1)

    cv2.imshow("Indian Flag", flag)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

generate()
