import cv2
import numpy as np
import matplotlib.pyplot as plt
def solve(s):
    img=cv2.imread(s)
    img=cv2.resize(img,(355,455))
    blurred=cv2.GaussianBlur(img,(5,5),0)


    edges=cv2.Canny(blurred,100,160)

    cv2.imshow("origin",img)
    cv2.imshow("canny",edges)
    cv2.waitKey(0)
s=r"C:\Users\mayan\OneDrive\Desktop\cv drone\tree.jpeg"
solve(s)