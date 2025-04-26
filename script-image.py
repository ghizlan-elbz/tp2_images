import cv2
import numpy as np

img = cv2.imread("images.jpeg")  
print("Dimensions d'origine :", img.shape)

B = img[:, :, 0]
G = img[:, :, 1]
R = img[:, :, 2]

img_gray = 0.2989 * R + 0.5870 * G + 0.1140 * B
img_gray = img_gray.astype(np.uint8)

img_compressed = img_gray[::2, ::2]

zoom_factor = 1.75
height, width = img_gray.shape
new_width = int(width * zoom_factor)
new_height = int(height * zoom_factor)
img_zoomed = cv2.resize(img_gray, (new_width, new_height), interpolation=cv2.INTER_LINEAR)

cv2.imshow("Image originale", img)
cv2.imshow("Niveaux de gris", img_gray)
cv2.imshow("Image compressée", img_compressed)
cv2.imshow("Image zoomée à 175%", img_zoomed)

cv2.waitKey(0)
cv2.destroyAllWindows()