import matplotlib.pyplot as plt
from skimage import io
from skimage.filters import threshold_otsu
from skimage.color import rgb2gray

filename = '../fountain.tif'
fountain = io.imread(filename)
grayscale = rgb2gray(fountain)
plt.figure()

fig, ax = plt.subplots(ncols=3)
ax[0].imshow(grayscale, cmap=plt.cm.gray)
otsu = threshold_otsu(grayscale)
binary = grayscale > otsu
ax[1].hist(otsu)



ax[2].imshow(binary, cmap=plt.cm.gray)
plt.show()