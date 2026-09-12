import numpy as np
import cv2

img = cv2.imread("input.jpg", 0)
min = np.min(img)
max = np.max(img)
st = (img - min) * (255.0 / (max - min))
st = st.astype(np.uint8)
cv2.imshow("Original", img)
cv2.imshow("Strached Image", st)
cv2.waitKey(0)
cv2.destroyAllWindows()
