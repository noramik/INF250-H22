import numpy as np
from skimage import io
import matplotlib.pyplot as plt
from skimage import filters, morphology, segmentation
from scipy import ndimage as ndi
from skimage.feature import peak_local_max
from skimage import measure
import math

# Import and plot original image
filepath = "../images/IMG_2754_nonstop_alltogether.JPG"
image = io.imread(filepath)
image = image.mean(axis=2)
image = image[200:-200, 200:-200] # Crop image to remove noisy borders.
fig, axes = plt.subplots(ncols=3)
ax = axes.ravel()
ax[0].imshow(image, cmap='gray')


# Otsu threshold
thresh = filters.threshold_otsu(image)
otsu_im = image > thresh
ax[1].imshow(otsu_im, cmap='gray')

# Watershed
distance = ndi.distance_transform_edt(otsu_im)
coords = peak_local_max(distance, footprint=np.ones((3, 3)), labels=otsu_im)
mask = np.zeros(distance.shape, dtype=bool)
mask[tuple(coords.T)] = True
markers, _ = ndi.label(mask)
labels = segmentation.watershed(-distance, markers, mask=otsu_im)

ax[2].imshow(labels, cmap='gray')

# Measure

labels2 = measure.label(otsu_im)
#ax[2].imshow(labels2, cmap='gray')
properties = measure.regionprops(labels2)

"""
for prop in properties:
    if prop.perimeter != 0:
        print(4*math.pi*prop.area/prop.perimeter**2)
"""
print(otsu_im)

mask_attempt = otsu_im*image
plt.figure()
plt.imshow(mask_attempt, cmap='gray')

plt.show()


