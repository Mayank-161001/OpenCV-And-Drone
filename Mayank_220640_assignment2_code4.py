import cv2
import numpy as np

def undistort(image_path):
    distorted_image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(distorted_image, cv2.COLOR_BGR2GRAY)
    chessboard_size = (6,6)

    objp = np.zeros((chessboard_size[0] * chessboard_size[1], 3), np.float32)
    objp[:, :2] = np.mgrid[0:chessboard_size[0], 0:chessboard_size[1]].T.reshape(-1, 2)

    
    objpoints = [] 
    imgpoints = [] 
    ret, corners = cv2.findChessboardCorners(gray_image, chessboard_size, None)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
    corners = cv2.cornerSubPix(gray_image, corners, (4,4),(-1, -1), criteria)


    if ret:
        objpoints.append(objp)
        imgpoints.append(corners)

        ret, camera_matrix, dist_coeffs, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray_image.shape[::-1], None, None)

        
        undistorted_image = cv2.undistort(distorted_image, camera_matrix, dist_coeffs)

        # Display the original and undistorted images
        cv2.imshow("Original Image", distorted_image)
        cv2.imshow("Undistorted Image", undistorted_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    else:
        print("Chessboard corners not found. Unable to undistort.")

# Example usage
undistort(r"C:\Users\mayan\OneDrive\Pictures\Screenshots\Screenshot 2023-12-28 205119.png")
