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

# Median filter
med_im = median(image)
ax[4].imshow(med_im, cmap='gray')
ax[4].set_title('Median filter')
for i in range(6):
    ax[i].axis('off')
plt.show()
