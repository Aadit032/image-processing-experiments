# trying to convert an image from rgb to bgr and see what it looks like

import cv2
import matplotlib.pyplot as plt

img = cv2.imread("images/input.jpg")

# OpenCV reads it as BGR.
# Convert BGR -> RGB for matplotlib.
# rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Deliberately swap RGB -> BGR and display it as if it were RGB.
# bgr_as_rgb = rgb[:, :, ::-1]

plt.imshow(img)
plt.axis("off")
# plt.show()
plt.savefig("images/result_new.png")
