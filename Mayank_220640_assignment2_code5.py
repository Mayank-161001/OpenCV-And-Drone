import cv2
import cv2.aruco as aruco
import numpy as np

def calibrate_camera(calibration_images_folder):
    # Manually set object points for ArUco marker
    objp = np.array([[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0]], dtype=np.float32)

    objpoints = []  
    imgpoints = [] 
       # Read calibration images
    images = [cv2.imread(f'{calibration_images_folder}/img{i}.jpg') for i in range(1, 9)]

    for img in images:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Detect ArUco markers in the image
        corners, ids, _ = aruco.detectMarkers(gray, aruco.Dictionary_get(aruco.DICT_4X4_50))

        if ids is not None and len(ids) > 0:
            # Use the first detected marker's corners for calibration
            corners = corners[0]

            # Add object points and image points
            objpoints.append(objp)
            imgpoints.append(corners)

    # Calibrate camera
    ret, camera_matrix, dist_coeffs, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

    return camera_matrix, dist_coeffs

def markers(image_path, camera_matrix, dist_coeffs):
    # Read the image
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Define the ArUco dictionary
    aruco_dict = aruco.Dictionary_get(aruco.DICT_4X4_50)

    parameters = aruco.DetectorParameters_create()

    # Detect ArUco markers in the image
    corners, ids, _ = aruco.detectMarkers(gray_image, aruco_dict, parameters=parameters)


    if ids is not None and len(ids) > 0:
        # Draw bounding box around the detected marker
        image = aruco.drawDetectedMarkers(image, corners, ids)
        rvec, tvec, _ = aruco.estimatePoseSingleMarkers(corners, 1, camera_matrix, dist_coeffs)

        # Draw axes for the detected marker
        for i in range(len(ids)):
            image = cv2.drawFrameAxes(image, camera_matrix, dist_coeffs, rvec[i], tvec[i], 1)
            
        # Compute center of the marker
        xc, yc = int(np.mean(corners[0][:, 0])), int(np.mean(corners[0][:, 1]))
        w=image.shape[0]
        h=image.shape[1]
        print(w,h)
        print("centre",xc,yc)
        cv2.imshow("Detected Marker", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        
        return xc, yc, rvec, tvec

    else:
        print("No ArUco marker found in the image.")
        return None


calibration_images_folder = r"C:\Users\mayan\OneDrive\Desktop\cv drone\aruco"
camera_matrix, dist_coeffs = calibrate_camera(calibration_images_folder)
markers(r"C:\Users\mayan\OneDrive\Desktop\cv drone\aruco\img1.jpg", camera_matrix, dist_coeffs)
