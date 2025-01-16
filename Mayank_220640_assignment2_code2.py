import cv2
import numpy as np

# Global variables to store rotated flags
rotated_flag_0 = None
rotated_flag_90 = None
rotated_flag_180 = None
rotated_flag_270 = None

def rotate(img, angle):
    height, width = img.shape[:2]

    # Calculate the rotation matrix
    rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), angle, 1)

    # Apply rotation to the image
    rotated_img = cv2.warpAffine(img, rotation_matrix, (width, height), borderMode=cv2.BORDER_CONSTANT, borderValue=(255, 255, 255))

    return rotated_img

def rotatedFlags():
    global rotated_flag_0, rotated_flag_90, rotated_flag_180, rotated_flag_270
    flag=cv2.imread(r"C:\Users\mayan\OneDrive\Desktop\cv drone\ass4\output1,2,4,5.png")
    flag=cv2.resize(flag,(300,300))

  
    rotated_flag_0 = rotate(flag, 0)
    rotated_flag_90 = rotate(flag, 90)
    rotated_flag_180 = rotate(flag, 180)
    rotated_flag_270 = rotate(flag, 270)
    


# Call the rotatedFlags function to generate rotated flags
rotatedFlags()
cv2.imshow("Rotated Flag at 0 degrees", rotated_flag_0)
cv2.imshow("Rotated Flag at 90 degrees", rotated_flag_90)
cv2.imshow("Rotated Flag at 180 degrees", rotated_flag_180)
cv2.imshow("Rotated Flag at 270 degrees", rotated_flag_270)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Display or use the rotated flags as needed
