import numpy as np
from skimage import io
import matplotlib.pyplot as plt
from skimage import filters, morphology, segmentation
from scipy import ndimage as ndi
from skimage.feature import peak_local_max
from skimage import measure


filepath = "../images/IMG_2754_nonstop_alltogether.JPG"
image = io.imread(filepath)
image = image[:,:,2] #Using the blue channel of the image.
image = image[200:-200, 200:-200] # Crop image to remove noisy borders.
fig, axes = plt.subplots(ncols=3)
ax = axes.ravel()
ax[0].imshow(image, cmap='gray')


# Otsu threshold
thresh = filters.threshold_otsu(image)
otsu_im = image > thresh
ax[1].imshow(otsu_im, cmap='gray')


plt.show()