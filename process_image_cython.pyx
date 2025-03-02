from libc.math cimport exp
import numpy as np
cimport numpy as cnp
from PIL import Image
from scipy.ndimage import convolve, median_filter

SOBEL_X = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], dtype=np.float64)
SOBEL_Y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]], dtype=np.float64)

def read_image(path: str) -> np.ndarray:
    """Reads a grayscale image and returns it as a 2D NumPy array."""
    img = Image.open(path).convert('L')
    return np.array(img, dtype=np.float64)

def save_image(image: np.ndarray, path: str) -> None:
    """Saves a NumPy array as a grayscale image."""
    img = Image.fromarray(image.astype(np.uint8))
    img.save(path)

def create_gaussian_kernel(size: int, sigma: float = 1) -> np.ndarray:
    """Creates a Gaussian kernel."""
    cdef int i, j
    cdef double[:, :] kernel = np.zeros((size, size), dtype=np.float64)
    cdef int center = size // 2
    cdef double sum_val = 0.0
    cdef double x, y
    
    for i in range(size):
        for j in range(size):
            x = i - center
            y = j - center
            kernel[i, j] = exp(-(x**2 + y**2) / (2 * sigma**2))
            sum_val += kernel[i, j]
    
    return np.asarray(kernel) / sum_val  # Convert to NumPy array before division

def apply_filter(image: np.ndarray, kernel: np.ndarray) -> np.ndarray:
    """Applies a convolution filter to an image using Cython."""
    cdef double[:, :] img_view = image.astype(np.float64)
    cdef double[:, :] kernel_view = kernel.astype(np.float64)
    return np.clip(convolve(img_view, kernel_view, mode='constant', cval=0.0), 0, 255).astype(np.uint8)

def apply_sobel(image: np.ndarray) -> np.ndarray:
    """Applies the Sobel filter to detect edges."""
    cdef double[:, :] img_view = image.astype(np.float64)
    grad_x = convolve(img_view, SOBEL_X, mode='constant', cval=0.0)
    grad_y = convolve(img_view, SOBEL_Y, mode='constant', cval=0.0)
    return np.clip(np.sqrt(grad_x**2 + grad_y**2), 0, 255).astype(np.uint8)

def apply_median_filter(image: np.ndarray, size: int) -> np.ndarray:
    """Applies a median filter to an image."""
    return median_filter(image, size=size).astype(np.uint8)