import cv2
import numpy as np
from matplotlib import pyplot as plt

def hybrid(s1, s2):
    img_low = cv2.imread(s1,0)
    img_low = cv2.resize(img_low, (256, 256))
    img_low_ft = np.fft.fft2(img_low)

    img_low_shifted = np.fft.fftshift(img_low_ft)
    size1 = img_low_shifted.shape
    k = lpf(size1, 0.38)
    img_low_filter = img_low_shifted * k
    inv_low = np.fft.ifftshift(img_low_filter)
    result_low = np.abs(np.fft.ifft2(inv_low))

    img_high = cv2.imread(s2, 0)
    img_high = cv2.resize(img_high, (256, 256))
    img_high_ft = np.fft.fft2(img_high)
    img_high_shifted = np.fft.fftshift(img_high_ft)
    size2 = img_high_shifted.shape
    h = hpf(size2, 0.45)
    img_high_filter = img_high_shifted * h
    inv_high = np.fft.ifftshift(img_high_filter)
    result_high = np.abs(np.fft.ifft2(inv_high))

    return [img_low_shifted, k, img_low_filter, result_low, img_high_shifted, h, img_high_filter, result_high, result_low + result_high]

def lpf(size, freq):
    row_cut = int(size[0] * freq)
    col_cut = int(size[1] * freq)

    f = np.ones(size)
    f[:row_cut, :] = 0
    f[-row_cut:, :] = 0
    f[:, :col_cut] = 0
    f[:, -col_cut:] = 0
    return f

def hpf(size, freq):
    row_cut = int(size[0] * freq)
    col_cut = int(size[1] * freq)

    f = np.ones(size)
    f[:row_cut, :] = 0
    f[-row_cut:, :] = 0
    f[:, :col_cut] = 0
    f[:, -col_cut:] = 0
    return 1 - f

s1 = r"C:\Users\mayan\OneDrive\Desktop\cv drone\oppenheimer.jpg"
s2 = r"C:\Users\mayan\OneDrive\Desktop\cv drone\allu.jpg"
result_list = hybrid(s1, s2)

plt.figure(figsize=(10, 10))

plt.subplot(342), plt.imshow(np.log(1 + np.abs(result_list[1])), cmap='gray')
plt.title('lpf'), plt.xticks([]), plt.yticks([])
plt.subplot(341), plt.imshow(np.log(1 + np.abs(result_list[0])), cmap='gray')
plt.title('Fourier Transform (Shifted)'), plt.xticks([]), plt.yticks([])

plt.subplot(343), plt.imshow(np.log(1 + np.abs(result_list[2])), cmap='gray')
plt.title('apply lpf'), plt.xticks([]), plt.yticks([])
plt.subplot(344), plt.imshow(np.log(1 + np.abs(result_list[3])), cmap='gray')
plt.title('final'), plt.xticks([]), plt.yticks([])

plt.subplot(346), plt.imshow(np.log(1 + np.abs(result_list[5])), cmap='gray')
plt.title('hpf'), plt.xticks([]), plt.yticks([])
plt.subplot(345), plt.imshow(np.log(1 + np.abs(result_list[4])), cmap='gray')
plt.title('Fourier Transform (Shifted)'), plt.xticks([]), plt.yticks([])

plt.subplot(347), plt.imshow(np.log(1 + np.abs(result_list[6])), cmap='gray')
plt.title('apply hpf'), plt.xticks([]), plt.yticks([])
plt.subplot(348), plt.imshow(np.log(1 + np.abs(result_list[7])), cmap='gray')
plt.title('final'), plt.xticks([]), plt.yticks([])
plt.subplot(349), plt.imshow(np.log(1 + np.abs(result_list[3])), cmap='gray')
plt.title('final result1'), plt.xticks([]), plt.yticks([])
plt.subplot(3,4,10), plt.imshow(np.log(1 + np.abs(result_list[7])), cmap='gray')
plt.title('final result 2'), plt.xticks([]), plt.yticks([])


plt.subplot(3,4,11), plt.imshow(np.log(1 + np.abs(result_list[8])), cmap='gray')
plt.title('hybrid'), plt.xticks([]), plt.yticks([])

plt.show()
