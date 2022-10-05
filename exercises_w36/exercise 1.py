from skimage import io
import matplotlib.pyplot as plt
import numpy as np

filename = '../fall.tiff'
fall = io.imread(filename)

plt.figure()
#plt.imshow(fall)

#shape of image matrix
print(fall.shape)



# Extracting red colour
fall_red = fall[:,:,0]
max(fall_red.flatten())
min(fall_red.flatten())

plt.imshow(fall_red, vmin=0, vmax=255)
plt.show()

# Extracting green colour

fall_green = fall[:,:,1]
max(fall_green.flatten())
min(fall_green.flatten())

plt.imshow(fall_green, vmin=0, vmax=255)
plt.show()


#Extracting blue colour

fall_blue = fall[:,:,2]
max(fall_blue.flatten())
min(fall_blue.flatten())

plt.imshow(fall_blue, vmin=0, vmax=255)
plt.show()