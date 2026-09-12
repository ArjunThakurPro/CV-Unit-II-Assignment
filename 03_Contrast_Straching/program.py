import numpy as np
import cv2

img = cv2.imread("input.jpg", 0)
min = np.min(img)
max = np.max(img)
st = (img - min) * (255.0 / (max - min))
st = st.astype(np.uint8)
cv2.imwrite("Strached Image", st)
