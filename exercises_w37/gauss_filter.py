import numpy as np
from skimage import io
from skimage.filters import gaussian
import matplotlib.pyplot as plt

filename = '../fountain.tif'
fountain = io.imread(filename)
plt.figure()
plt.imshow(fountain)
plt.show()
print(fountain)

gauss = gaussian(image=fountain, sigma=5.0, multichannel=True)

plt.imshow(gauss)
plt.show()

# Gaussian filter gjør bildet mer blurry
