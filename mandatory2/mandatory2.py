import numpy as np
from skimage import io
import matplotlib.pyplot as plt

filepath = "../images/IMG_2754_nonstop_alltogether.JPG"
image = io.imread(filepath)
image = image.mean(axis=2)
plt.imshow(image, cmap='gray')
plt.show()
