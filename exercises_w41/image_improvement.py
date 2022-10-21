from skimage import io
import matplotlib.pyplot as plt
import skimage.morphology as mrph
from skimage import filters


filepath = "../images/FingerPrint.tif"
image = io.imread(filepath)

n = 2
fig, axes = plt.subplots(ncols=n, nrows=n)
ax = axes.ravel()
ax[0].imshow(image, cmap='gray')


# Remove noise
less_noise_im = mrph.opening(image, mrph.square(2))
ax[1].imshow(less_noise_im, cmap='gray')

# Sharpening
sharpened = filters.unsharp_mask(less_noise_im)
ax[2].imshow(sharpened, cmap='gray')


plt.show()