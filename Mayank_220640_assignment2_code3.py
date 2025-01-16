import cv2
import numpy as np
import matplotlib.pyplot as plt

# variables to store rotated images
rotated_0_deg = None
rotated_90_deg = None
rotated_180_deg = None
rotated_270_deg = None

# Rotation Function taken from code2

def rotate(img, angle):
    height, width = img.shape[:2]

    # Calculate the rotation matrix
    rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), angle, 1)

    # Apply rotation to the image
    rotated_img = cv2.warpAffine(img, rotation_matrix, (width, height), borderMode=cv2.BORDER_CONSTANT, borderValue=(255, 255, 255))

    return rotated_img
# Rotated flag function from code2
def rotatedFlags():
    global rotated_0_deg, rotated_90_deg, rotated_180_deg, rotated_270_deg
    # Load the Indian Flag image generated in code1
    original_image = cv2.imread(r"C:\Users\mayan\OneDrive\Desktop\cv drone\ass4\output1,2,4,5.png")
    # Storing Rotate images for use later
    rotated_0_deg = rotate(original_image, 0)
    rotated_90_deg = rotate(original_image, 90)
    rotated_180_deg = rotate(original_image, 180)
    rotated_270_deg = rotate(original_image, 270)


# Function for traversing vertically to pick out the color from image in order to obtain orientaion of image
def vertical_traversal(image):

    midline_index = image.shape[1] // 2

    for i in range(image.shape[0]):
        pixel_color = image[i, midline_index]
        if np.array_equal(pixel_color, [255,62,62]) and np.array_equal(pixel_color, [0,0,0]):
            continue

        else:
            if np.array_equal(pixel_color,[52, 153, 255]):
                ver_orientation = "0deg"
                break
            elif np.array_equal(pixel_color,[1, 128, 0]):
                ver_orientation = "180deg"
                break
            elif np.array_equal(pixel_color, [255,255,255]):
                ver_orientation = horizontal_traversal(image)
                break
    
    return ver_orientation

def horizontal_traversal(image):

    midline_index = image.shape[0] // 2

    for i in range(image.shape[1]):
        pixel_color = image[midline_index,i]
        if np.array_equal(pixel_color, [255,62,62]) and np.array_equal(pixel_color, [0,0,0]):
            continue
        else:
            if np.array_equal(pixel_color, [52, 153, 255]):
                hor_orientation = "90deg"
                break
            elif np.array_equal(pixel_color,[1, 128, 0]):
                hor_orientation = "270deg"
                break    
    return hor_orientation
# Defining Function for generating unskewed image
def unskew(s):
    
    img = cv2.imread(s)
    img = cv2.resize(img,(600,600))
    # calling the rotatedflag function to obtain refernce images for unskewing.
    rotatedFlags()
    orientation = vertical_traversal(img)
    
    if orientation == "0deg":
        cv2.imshow("unskewed",rotated_0_deg)
    elif orientation == "90deg":
        cv2.imshow("unskewed",rotated_90_deg)
    elif orientation == "180deg":
        cv2.imshow("unskewed",rotated_180_deg)
    elif orientation == "270deg":
        cv2.imshow("unskewed",rotated_270_deg)
    cv2.imshow("skewed input",img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
 
unskew(r"C:\Users\mayan\OneDrive\Desktop\cv drone\ass4\tc2.jpg")
