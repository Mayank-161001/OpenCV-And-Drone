import cv2
import numpy as np

def adjust_image(s):
    image = cv2.imread(s)
    brightness_factor = 0.5
    darkened_image = np.clip(image * brightness_factor, 0, 255).astype(np.uint8)
    contrast_factor = 1.5
    adjusted_image = cv2.convertScaleAbs(darkened_image, alpha=contrast_factor, beta=0)

    hsv_image = cv2.cvtColor(adjusted_image, cv2.COLOR_BGR2HSV)
    saturation_factor = 1.5
    hsv_image[:, :, 1] = np.clip(saturation_factor * hsv_image[:, :, 1], 0, 255).astype(np.uint8)
    final_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)

    return final_image

s = r"C:\Users\mayan\OneDrive\Desktop\cv drone\nature.jpg"
output_image = adjust_image(s)
cv2.imshow('Original Image', cv2.imread(s))
cv2.imshow('Final Result', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
