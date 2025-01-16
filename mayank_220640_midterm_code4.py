import cv2
import numpy as np

def shapes(s):
    image = cv2.imread(s)
    image=cv2.resize(image,(600,500))
    cv2.imshow("real image",image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    edges = cv2.Canny(blurred, 50, 150)
    
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    shape_names = {
        3: "Triangle",
        4: "Rectangle",
        5: "Pentagon",
        6: "Hexagon",
        7: "Heptagon",
        8: "Octagon",
        9: "Nonagon"
    }

    for contour in contours:
        epsilon = 0.04 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)
        num_sides = len(approx)
        
        M = cv2.moments(contour)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])

        shape_name = shape_names.get(num_sides, "Unknown")
        print(f"Shape: {shape_name}, Center: ({cX}, {cY})")
        cv2.drawContours(image, [contour], -1, (0, 255, 0), 2)
        cv2.circle(image, (cX, cY), 5, (255, 255, 255), -1)
        cv2.putText(image, shape_name, (cX - 20, cY - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:2]
    for i, contour in enumerate(contours, 1):
        M = cv2.moments(contour)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
        cv2.putText(image, f"Largest-{i}", (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
        cv2.circle(image, (cX, cY), 5, (0, 0, 0), -1)

   
    cv2.imshow('Identified Shapes', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


image_path = r"C:\Users\mayan\OneDrive\Desktop\cv drone\gem2.png"
shapes(image_path)
