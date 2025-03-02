import numpy as np
from PIL import Image

SOBEL_X = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
SOBEL_Y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

def read_image(path: str) -> np.ndarray:
    """Reads a grayscale image and returns it as a 2D NumPy array."""
    img = Image.open(path).convert('L')
    return np.array(img, dtype=np.float32)

def save_image(image: np.ndarray, path: str) -> None:
    """Saves a NumPy array as a grayscale image."""
    img = Image.fromarray(image.astype(np.uint8))
    img.save(path)

def create_gaussian_kernel(size: int, sigma: float = 1) -> np.ndarray:
    """Creates a Gaussian kernel."""
    ax = np.linspace(-(size // 2), size // 2, size)
    xx, yy = np.meshgrid(ax, ax)
    kernel = np.exp(-(xx**2 + yy**2) / (2 * sigma**2))
    return kernel / kernel.sum()

def apply_filter(image: np.ndarray, kernel: np.ndarray) -> np.ndarray:
    """Applies a convolution filter to an image using NumPy."""
    from scipy.ndimage import convolve
    return convolve(image, kernel, mode='constant', cval=0.0)

def apply_sobel(image: np.ndarray) -> np.ndarray:
    """Applies the Sobel filter to detect edges."""
    grad_x = apply_filter(image, SOBEL_X)
    grad_y = apply_filter(image, SOBEL_Y)
    return np.clip(np.sqrt(grad_x**2 + grad_y**2), 0, 255)

def apply_median_filter(image: np.ndarray, size: int) -> np.ndarray:
    """Applies a median filter to an image."""
    from scipy.ndimage import median_filter
    return median_filter(image, size=size)
