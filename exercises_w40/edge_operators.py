import matplotlib.pyplot as plt
import numpy as np
from skimage import io
from skimage.filters import sobel, prewitt, laplace
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
    if operator == 1:
        filtered = sobel(image)
    elif operator == 2:
        filtered = prewitt(image)
    elif operator == 3:
        filtered = canny(image)
    elif operator == 4:
        filtered = laplace(image)
    else:
        raise ValueError('The value of the operator must be between 1 and 4.')
    
    return filtered

def sharpen():
    pass

if __name__ == '__main__':
    filepath = '../images/AthenIR.png'
    ir_im = io.imread(filepath)
    filtered = edge_operator(ir_im, 4)
    fig, axes = plt.subplots(ncols=2)
    ax = axes.ravel()

    ax[0].imshow(ir_im, cmap='hot')
    ax[1].imshow(filtered, cmap='hot')
    plt.show()
