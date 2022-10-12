from skimage import io
import numpy as np
import matplotlib.pyplot as plt
from hist_eq import hist_equalisation
from skimage.filters import gaussian, median

# Plotting original image
filepath = '../images/UrStoy.tif'
image = io.imread(filepath)
fig, axes = plt.subplots(nrows=2, ncols=3)
ax = axes.ravel()
ax[0].imshow(image, cmap='gray')
ax[0].set_title('Original image')

#Histogram equalisation
hist_im = hist_equalisation(image)
ax[1].imshow(hist_im, cmap='gray')
ax[1].set_title('Histogram equalisation')

# Gaussian filter
gauss_im = gaussian(image)
ax[2].imshow(gauss_im, cmap='gray')
ax[2].set_title('Gaussian filter')



# Mean filter

# Implementation of mean filter
# This ignores the border pixels.
shape = image.shape
im = image
for i in range(1, shape[0]-1):
    for j in range(1, shape[1]-1):
        mean = (1/9)*(im[i-1, j-1]+im[i-1, j]+im[i-1, j+1]+im[i, j-1]+im[i, j]+im[i, j+1]+im[i+1, j-1]
                +im[i+1, j]+im[i+1, j+1])
        im[i, j] = mean

ax[3].imshow(im, cmap='gray')
ax[3].set_title('Mean filter')


# Median filter
med_im = median(image)
ax[4].imshow(med_im, cmap='gray')
ax[4].set_title('Median filter')
for i in range(6):
    ax[i].axis('off')



# Residuals between hist im and gaussian im
fig2, axes2 = plt.subplots(ncols=3)
new_ax = axes2.ravel()
new_ax[0].imshow(hist_im-gauss_im, cmap='gray')
# Residuals between hist im and mean im
new_ax[1].imshow(hist_im-im, cmap='gray')
# Residuals between hist im and median im
new_ax[2].imshow(hist_im-med_im, cmap='gray')
plt.show()