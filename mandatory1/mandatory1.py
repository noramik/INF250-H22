# -*- coding: utf-8 -*-

"""
Skeleton for first part of the blob-detection coursework as part of INF250
at NMBU (Autumn 2017).
"""

__author__ = "Nora Mikarlsen"
__email__ = "nora.mikarlsen@nmbu.no"

import numpy as np
from skimage import io
import matplotlib.pyplot as plt
from skimage.color import rgb2gray


def threshold(image, th=None):
    """Returns a binarised version of given image, thresholded at given value.

    Binarises the image using a global threshold `th`. Uses Otsu's method
    to find optimal thrshold value if the threshold variable is None. The
    returned image will be in the form of an 8-bit unsigned integer array
    with 255 as white and 0 as black.

    Parameters:
    -----------
    image : np.ndarray
        Image to binarise. If this image is a colour image then the last
        dimension will be the colour value (as RGB values).
    th : numeric
        Threshold value. Uses Otsu's method if this variable is None.

    Returns:
    --------
    binarised : np.ndarray(dtype=np.uint8)
        Image where all pixel values are either 0 or 255.
    """
    # Setup
    shape = np.shape(image)

    if len(shape) == 3:
        image = image.mean(axis=2)
    elif len(shape) > 3:
        raise ValueError('Must be at 2D image')

    if th is None:
        th = otsu(image)

    # Start thresholding
    ## WRITE YOUR CODE HERE
    binarised = image > th
    return binarised


def histogram(image):
    """Returns the image histogram with 256 bins.
    """
    # Setup
    shape = np.shape(image)
    hist = np.zeros(256)

    if len(shape) == 3:
        image = image.mean(axis=2)
    elif len(shape) > 3:
        raise ValueError('Must be at 2D image')

    # Start to make the histogram
    ## WRITE YOUR CODE HERE
    for i in range(shape[0]):
        for j in range(shape[1]):
            ix = int(image[i, j])
            hist[ix] += 1
    return hist


def otsu(image):
    """Finds the optimal thresholdvalue of given image using Otsu's method.
    """
    hist = histogram(image)
    th = 0

    ## WRITE YOUR CODE HERE
    max_sigmab = 0
    image = image.mean(axis=2)
    npix = image.size
    intensity_arr = np.arange(256)
    sigma_b = 0
    for temp_th in range(256):
        nb = np.sum(hist[:temp_th]) #number of pixels in background
        nf = np.sum(hist[temp_th:]) #number of pixels in foreground
        wb = nb/npix # weight background
        wf = nf/npix # weight foreground
        if nb > 0 and nf > 0:
            mean_b = np.sum(intensity_arr[:temp_th]*hist[:temp_th])/nb # mean background
            mean_f = np.sum(intensity_arr[temp_th:]*hist[temp_th:])/nf # mean foreground
            sigma_b = wb*wf*((mean_b-mean_f)**2) # between class variance
        if sigma_b > max_sigmab:
            max_sigmab = sigma_b
            th = temp_th
    return th



if __name__ == '__main__':
    filepath = '../images/gingerbreads.jpg'
    gingerbread = io.imread(filepath)
    hist = histogram(gingerbread)
    otsu_th = otsu(gingerbread)
    thresholded_im = threshold(gingerbread, otsu_th)
    gingerbread = rgb2gray(gingerbread)
    fig = plt.figure()
    plt.imshow(thresholded_im, cmap='gray')
    plt.show()
    fig.savefig('thresholded_im.png')