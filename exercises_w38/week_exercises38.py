from skimage import io
import matplotlib.pyplot as plt
import numpy as np
from skimage.filters import threshold_otsu


filepath = '../images/airfield.tif'
image = io.imread(filepath)

# Original image
fig, axes = plt.subplots(ncols= 3, nrows=2)
ax = axes.ravel()
ax[0].imshow(image, cmap='gray')
ax[0].set_title('Original image')

# Histogram
ax[1].hist(image.ravel(), bins=256)
ax[1].set_title('Histogram')
contr_im = image+30

# Adjusting brightness
ax[2].imshow(contr_im, cmap='gray')
ax[2].set_title('Adjust brightness')


# Adjusting contrast


# Histogram equalisation

histogram = np.zeros(256)
shape = np.shape(image)
for i in range(shape[0]):
    for j in range(shape[1]):
        pixval = int(image[i,j])
        histogram[pixval] += 1

cumhist = np.zeros(256)
cumhist[0] = histogram[0]
for i in range(255):
    cumhist[i+1] = cumhist[i] + histogram[i+1]

K = 256
M = shape[0]
N = shape[1]
image_he = np.zeros(image.shape)
for i in range(M):
    for j in range(N):
        a = int(image[i, j])
        b = cumhist[a]*(K-1)/M*N
        image_he[i, j] = b
ax[3].imshow(image_he, cmap='gray')
ax[3].set_title('Histogram equalisation')

ax[4].hist(image_he.ravel(), bins=256)


# Otsu threshold
thresh = threshold_otsu(image)
binary = image > thresh
ax[5].set_title('Otsu Method')
ax[5].imshow(binary, cmap='gray')
plt.show()