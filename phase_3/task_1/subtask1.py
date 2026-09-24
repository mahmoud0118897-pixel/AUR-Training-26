import cv2 
import matplotlib.pyplot as plt
ksize=(5,5)
sigmax=1
K=5
lowthreshold=80
highthreshold=160
img=cv2.imread('image1.jpg')
if img is None:
    print("Error: Could not read the image.")
    exit()
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
avr_blur=cv2.blur(gray_img,ksize)
gaus_blur=cv2.GaussianBlur(gray_img,ksize,sigmax)
median_blur=cv2.medianBlur(gray_img,K)
canny_avr_blur=cv2.Canny(avr_blur,lowthreshold,highthreshold) 
canny_gaus_blur=cv2.Canny(gaus_blur,lowthreshold,highthreshold)
canny_median_blur=cv2.Canny(median_blur,lowthreshold,highthreshold)
#result_avr_blur=cv2.addWeighted(gray_img, 0.5, canny_avr_blur, 0.5, 0)
result_gaus_blur=cv2.addWeighted(gray_img, 0.5, canny_gaus_blur, 0.5, 0)
#result_median_blur=cv2.addWeighted(gray_img, 0.5, canny_median_blur, 0.5, 0)
plt.figure(figsize=(12, 8))


plt.subplot(2, 4, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')


plt.subplot(2, 4, 2)
plt.imshow(avr_blur, cmap='gray')
plt.title('Average Blur')
plt.axis('off')

plt.subplot(2, 4, 3)
plt.imshow(gaus_blur, cmap='gray')
plt.title('Gaussian Blur')
plt.axis('off')


plt.subplot(2, 4, 4)
plt.imshow(median_blur, cmap='gray')
plt.title('Median Blur')
plt.axis('off')

plt.subplot(2, 4, 5)
plt.imshow(result_gaus_blur, cmap='gray')
plt.title('Result_Gaussian_Blur')
plt.axis('off')

plt.subplot(2, 4, 6)
plt.imshow(canny_avr_blur, cmap='gray')
plt.title('Canny (Average)')
plt.axis('off')


plt.subplot(2, 4, 7)
plt.imshow(canny_gaus_blur, cmap='gray')
plt.title('Canny (Gaussian)')
plt.axis('off')

plt.subplot(2, 4, 8)
plt.imshow(canny_median_blur, cmap='gray')
plt.title('Canny (Median)')
plt.axis('off')

plt.tight_layout()
plt.show()