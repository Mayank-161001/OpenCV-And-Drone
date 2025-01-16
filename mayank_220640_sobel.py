import cv2
import numpy as np
from matplotlib import pyplot as plt
def sobel(s1):
    img=cv2.imread(s1,0)

    img2=cv2.normalize(img,None, -1, 10, cv2.NORM_MINMAX)

    fx=cv2.Sobel(img2,-1,1,0)
    # fx2=cv2.normalize(fx,None, 0, 500, cv2.NORM_MINMAX)
    fy=cv2.Sobel(img2,-1,0,1)
    # fy2=cv2.normalize(fy,None, 0, 500, cv2.NORM_MINMAX)
    mag=np.sqrt(fx**2+fy**2)
    # mag=cv2.addWeighted(fx,1,fy,1,0)


    # mag2=cv2.normalize(,None, 0, 400, cv2.NORM_MINMAX)
    plt.subplot(121),plt.imshow(img,cmap='gray')
    plt.title('Original'),plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(mag,cmap='gray')
    plt.title('edge detected'),plt.xticks([]), plt.yticks([])
    plt.show()
s=r"C:\Users\mayan\OneDrive\Desktop\cv drone\oppenheimer.jpg"
sobel(s)