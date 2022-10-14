import numpy as np

def hist_equalisation(image):
    """
    Takes in an image, computes the original histogram for the image, then a cumulative histogram
    for the image, then performs a histogram equalisation on the image.

    :param image: original image
    :return: image_he: histogram equalised image
    """
    # Histogram equalisation
    if len(np.shape(image)) == 3:
        image = image.mean(axis=2)

    histogram = np.zeros(256)
    shape = np.shape(image)
    for i in range(shape[0]):
        for j in range(shape[1]):
            pixval = int(image[i, j])
            histogram[pixval] += 1

    cumhist = np.zeros(256)
    cumhist[0] = histogram[0]
    for i in range(255):
        cumhist[i + 1] = cumhist[i] + histogram[i + 1]

    K = 256
    M = shape[0]
    N = shape[1]
    image_he = np.zeros(image.shape)
    for i in range(M):
        for j in range(N):
            a = int(image[i, j])
            b = cumhist[a] * (K - 1) / M * N
            image_he[i, j] = b
    return image_he