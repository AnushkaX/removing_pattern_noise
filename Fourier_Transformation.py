#fourier transformation
import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('H:/Sem5/Day4/Images/face.jpg', cv2.IMREAD_GRAYSCALE)

f = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
sf = np.fft.fftshift(f)
mag = 20*np.log(cv2.magnitude(sf[:,:,0],sf[:,:,1]))


cv2.circle(sf, (254,68), 10,(0,0,0), thickness=-1)
cv2.circle(sf, (337,72), 10,(0,0,0), thickness=-1)
cv2.circle(sf, (421,74), 10,(0,0,0), thickness=-1)
cv2.circle(sf, (249,125), 10,(0,0,0), thickness=-1)
cv2.circle(sf, (331,128), 10,(0,0,0), thickness=-1)
cv2.circle(sf, (413,130), 10,(0,0,0), thickness=-1)
cv2.circle(sf, (241,180), 10,(0,0,0), thickness=-1)
cv2.circle(sf, (407,185), 10,(0,0,0), thickness=-1)
cv2.circle(sf, (235,235), 10,(0,0,0), thickness=-1)
cv2.circle(sf, (319,239), 10,(0,0,0), thickness=-1)
cv2.circle(sf, (400,241), 10,(0,0,0), thickness=-1)
cv2.circle(sf, (230,292), 10,(0,0,0), thickness=-1)
cv2.circle(sf, (312,293), 10,(0,0,0), thickness=-1)
cv2.circle(sf, (393,296), 10,(0,0,0), thickness=-1)
sf[105:35,108:42,:] = 0


isf = np.fft.ifftshift(sf)
iisf = cv2.idft(isf)
img_t = cv2.magnitude(iisf[:,:,0],iisf[:,:,1])

plt.subplot(221),plt.imshow(img, cmap = 'gray')
plt.title('Input Image'), plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(mag, cmap = 'gray')
plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
plt.subplot(223),plt.imshow(img_t, cmap = 'gray')
plt.title('Final'), plt.xticks([]), plt.yticks([])

##plt.imshow(img, cmap='gray')
##plt.show()
##plt.imshow(mag, cmap='gray')
##plt.show()
##plt.imshow(img_t,cmap='gray')
plt.show()
