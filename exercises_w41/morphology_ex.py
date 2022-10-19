import matplotlib.pyplot as plt
from skimage import io
import skimage.morphology as mrph

# Import the image and plot original
filepath = "../images/rhino_d.tif"
image = io.imread(filepath)
fig, axes = plt.subplots(ncols=3, nrows=3)
ax = axes.ravel()
ax[0].imshow(image, cmap='gray')
ax[0].set_title('Original')
for ix in range(9):
    ax[ix].axis('off')

# Dilation (square(3))
rhinodil = mrph.dilation(image, mrph.square(3))
ax[1].imshow(rhinodil, cmap='gray')
ax[1].set_title('Dilation')


# Erosion (square(3))
rhinoer = mrph.erosion(image, mrph.square(3))
ax[2].imshow(rhinoer, cmap='gray')
ax[2].set_title('Erosion')

# Dilate, then erode (aka closing)
rhino3 = mrph.erosion(rhinodil, mrph.square(3))
ax[3].imshow(rhino3, cmap='gray')
ax[3].set_title('Dilation --> erosion')

# Erode, then dilate (aka opening)
rhino4 = mrph.dilation(rhinoer, mrph.square(3))
ax[4].imshow(rhino4, cmap='gray')
ax[4].set_title('Erosion --> dilation')

# Opening
rhino5 = mrph.opening(image, mrph.square(3))
ax[5].imshow(rhino5, cmap='gray')
ax[5].set_title('Opening')

# Closing
rhino6 = mrph.closing(image, mrph.square(3))
ax[6].imshow(rhino6, cmap='gray')
ax[6].set_title('Closing')

# Min

plt.show()