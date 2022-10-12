from skimage import io
import numpy as np
import matplotlib.pyplot as plt

filepath = '../images/UrStoy.tif'
image = io.imread(filepath)
fig, axes = plt.subplots(nrows=3, ncols=2)
ax = axes.ravel()
ax[0].imshow(image, cmap='gray')
ax[0].set_title('Original image')

ax[0].imshow(hist_im, cmap='gray')
ax[1].set_title('Histogram equalisation')


plt.show()
