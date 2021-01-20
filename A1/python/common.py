import numpy as np

def rgb_to_gray(I):
    """
    Converts a HxWx3 RGB image to a HxW grayscale image as
    described in the text.
    """
    gray = I.mean(axis = 2)
    return gray 

def central_difference(I):
    """
    Computes the gradient in the x and y direction using
    a central difference filter, and returns the resulting
    gradient images (Ix, Iy) and the gradient magnitude Im.
    """
    K = [0.5, 0, -0.5]
    Ix = np.convolve(I.ravel(),K, mode = "same").reshape(np.shape(I))
    Iy = np.convolve(I.ravel("F"),K, mode = "same").reshape(np.shape(I),order='F')
    Im = np.sqrt(Ix**2+Iy**2)
    return Ix, Iy, Im

def gaussian(I, sigma):
    """
    Applies a 2-D Gaussian blur with standard deviation sigma to
    a grayscale image I.
    """

    # Hint: The size of the kernel should depend on sigma. A common
    # choice is to make the half-width be 3 standard deviations. The
    # total kernel width is then 2*np.ceil(3*sigma) + 1.

    kernel = np.zeros(int(2*np.ceil(3*sigma)+1))
    for i in range(kernel.size):
        x = i - kernel.size//2
        kernel[i] = 1 / (2*np.pi*sigma**2) * np.exp(-x**2/(2*sigma**2))
    
    result = np.convolve(I.ravel(),kernel, mode = "same").reshape(np.shape(I))
    result = np.convolve(I.ravel("F"), kernel, mode = "same").reshape(np.shape(I),order='F')
    return result/np.max(result)

def extract_edges(Ix, Iy, Im, threshold):
    """
    Returns the x, y coordinates of pixels whose gradient
    magnitude is greater than the threshold. Also, returns
    the angle of the image gradient at each extracted edge.
    """
    edges = np.where(Im > threshold)
    theta = []
    for y,x in zip(edges[0], edges[1]):
        theta.append(np.arctan2(Iy[y,x], Ix[y,x]))
    return edges[1], edges[0] ,theta
