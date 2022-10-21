from skimage import io
import matplotlib.pyplot as plt
from skimage import morphology as mrph
from skimage import filters
from skimage.feature import canny

# Image contours.

filepath = "../images/rhino_detail.tif"
image = io.imread(filepath)

skel_im = mrph.skeletonize(image)
sobel_im = filters.sobel(image)
laplace_im = filters.laplace(image)
canny_im = canny(image, sigma=3)
canny_im2 = canny(image, sigma=1)
n = 3
m = 2
fig, axes = plt.subplots(ncols=n, nrows=m)
ax = axes.ravel()
sigma = r'$\sigma$'
ax[0].imshow(image, cmap='gray')
ax[0].set_title('Original')
ax[1].imshow(skel_im, cmap='gray')
ax[1].set_title('Skeletonized')
ax[2].imshow(sobel_im, cmap='gray')
ax[2].set_title('Sobel filter')
ax[3].imshow(laplace_im, cmap='gray')
ax[3].set_title('Laplace filter')
ax[4].imshow(canny_im, cmap='gray')
ax[4].set_title(f'Canny filter, {sigma} = 3')
ax[5].imshow(canny_im2, cmap='gray')
ax[5].set_title(f'Canny filter, {sigma} = 1')

for i in range(n*m):
    ax[i].axis('off')
plt.show()