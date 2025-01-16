import cv2
import numpy as np
from matplotlib import pyplot as plt
def hough_line(s):
    img=cv2.imread(s)
    img=cv2.resize(img,(1200,600))
    edges=cv2.Canny(img,50,150)
    

    # lines=cv2.HoughLines(edge,1,np.pi/180,200)
    #(img src,rho(dist from 0,0 accumulation in pixels),theta,threshold)

    lines = cv2.HoughLines(edges, 1, np.pi/180, 100)

    # Iterate over each line in the lines array
    for line in lines:
        print(line)
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))

        # Draw the line on the original image.
        cv2.line(img, (x1, y1), (x2, y2), (255, 0,0), 2)
    return img,edges

# Display the original image with the lines drawn.
s=r"C:\Users\mayan\OneDrive\Desktop\cv drone\gem2.png"
img,edges=hough_line(s)
plt.figure(figsize=(10, 50))
plt.subplot(122), plt.imshow(img, cmap='gray')
plt.title('Hough Trans'), plt.xticks([]), plt.yticks([])
plt.subplot(121), plt.imshow(edges, cmap='gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])


plt.show()

