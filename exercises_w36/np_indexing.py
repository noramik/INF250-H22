import numpy as np
from skimage import io
import matplotlib.pyplot as plt


filename = '../fiat.jpg'
fiat = io.imread(filename)

fiat_red = fiat[:,:,0]
print(f'Max = {max(fiat_red.flatten())}, min = {min(fiat_red.flatten())}, avg = {np.mean(fiat_red.flatten())}')

print(fiat.shape)

fiat[4,2, :] = 255


nrows, ncols, redundant = fiat.shape
row, col = np.ogrid[:nrows, :ncols]
cnt_row, cnt_col = nrows / 2, ncols / 2
outer_disk_mask = ((row - cnt_row)**2 + (col - cnt_col)**2 >
                    (nrows / 2)**2)
fiat[outer_disk_mask] = 0
plt.imshow(fiat)
plt.show()