import matplotlib.pyplot as plt
import numpy as np
from skimage import io
from skimage.filters import sobel, prewitt
from skimage.feature import canny

def edge_operator(image, operator):
    """Returns the reusult from one of the edge operators, prewitt, sobel,
    canny eller laplace

    Parameters:
    -----------
    image : np.ndarray
        Image to detect blobs in. If this image is a colour image then
        the last dimension will be the colour value (as RGB values).
    operator : numeric
    1 = sobel filter
    2 = prewitt filter
    3 = canny filter
    4 = laplace filter

    Returns:
    --------
    filtered : np.ndarray(np.uint)
    result image from the edge operator
    """

    image = image.mean(axis=2)
    filter_dict = {1: sobel, 2: prewitt, 3: canny}
    filtered = filter_dict[operator](image)
    
    return filtered



if __name__ == '__main__':
    filepath = '../images/AthenIR.png'
    ir_im = io.imread(filepath)
    filtered = edge_operator(ir_im, 3)
    fig, axes = plt.subplots(ncols=2)
    ax = axes.ravel()

    ax[0].imshow(ir_im, cmap=plt.cm.gray)
    ax[1].imshow(filtered, cmap=plt.cm.gray)
    plt.show()
