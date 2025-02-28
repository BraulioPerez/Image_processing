"""
PIL for image processing
math for calculating specific data
"""

from PIL import Image
import math


SOBEL_X = [
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]
]

SOBEL_Y = [
    [-1, -2, -1],
    [0, 0, 0],
    [1, 2, 1]
]

def read_image(path:str) -> list:
    """Reads a grayscale image and returns it as a 2D list."""
    img = Image.open(path).convert('L')
    width, height = img.size
    pixels = list(img.getdata())
    # Convert flat list to 2D list (height x width)
    return [pixels[i*width : (i+1)*width] for i in range(height)]

def save_image(image:list, path:str) -> None:
    """Saves a 2D list (grayscale image) to a file."""
    height = len(image)
    width = len(image[0]) if height > 0 else 0
    # Flatten the 2D list into a 1D list
    pixels = [pixel for row in image for pixel in row]
    img = Image.new('L', (width, height))
    img.putdata(pixels)
    img.save(path)
    return None

def multiply(matrix_a, matrix_b) -> list:
    """Multiplies 2 matrices more efficiently using enumerate and list comprehension"""
    rows_a = len(matrix_a)
    cols_b = len(matrix_b[0])
    cols_a = len(matrix_a[0])
    
    # Initialize result matrix using list comprehension
    result = [[sum(a * b for a, b in zip(matrix_a[i], (matrix_b[k][j] for k in range(cols_a))))
               for j in range(cols_b)]
              for i in range(rows_a)]
    
    return result

def create_gaussian_kernel(size, sigma=1) -> list:
    """Creates a Gaussian kernel of the specified size."""
    kernel = [[0] * size for _ in range(size)]
    center = size // 2
    sum_val = 0.0

    for i in range(size):
        for j in range(size):
            x = i - center
            y = j - center
            kernel[i][j] = math.exp(-(x**2 + y**2) / (2 * sigma**2))
            sum_val += kernel[i][j]

    # Normalize the kernel
    for i in range(size):
        for j in range(size):
            kernel[i][j] /= sum_val

    return kernel

def apply_gaussian(image, kernel) -> list:
    """Applies a Gaussian filter to the image using the provided kernel."""
    height = len(image)
    width = len(image[0]) if height > 0 else 0
    kernel_size = len(kernel)
    pad = kernel_size // 2
    new_image = []

    # Pad the image with zeros
    padded_image = [[0] * (width + 2 * pad) for _ in range(height + 2 * pad)]
    for i in range(height):
        for j in range(width):
            padded_image[i + pad][j + pad] = image[i][j]

    for i in range(height):
        new_row = []
        for j in range(width):
            total = 0
            for dx in range(-pad, pad + 1):
                for dy in range(-pad, pad + 1):
                    x = i + pad + dx
                    y = j + pad + dy
                    pixel = padded_image[x][y]
                    total += pixel * kernel[dx + pad][dy + pad]
            # Clamp to 0-255
            new_pixel = max(0, min(int(total), 255))
            new_row.append(new_pixel)
        new_image.append(new_row)
    return new_image

def apply_sobel(image) -> list:

    """
    takes an image as a parameter and applies
    the sobel filter to return a list with the new values
    """

    height = len(image)
    width = len(image[0]) if height > 0 else 0
    new_image = []
    
    # Adding padding to handle edgees
    padded_image = [[0] * (width + 2) for _ in range(height + 2)]
    for i in range(height):
        for j in range(width):
            padded_image[i + 1][j + 1] = image[i][j]

    for i in range(height):
        new_row = []
        for j in range(width):
            region = [
                [padded_image[i][j], padded_image[i][j+1], padded_image[i][j+2]],
                [padded_image[i+1][j], padded_image[i+1][j+1], padded_image[i+1][j+2]],
                [padded_image[i+2][j], padded_image[i+2][j+1], padded_image[i+2][j+2]]
            ]

            gradient_x = 0
            gradient_y = 0
            for x in range(3):
                for y in range(3):
                    gradient_x += region[x][y] * SOBEL_X[x][y]
                    gradient_y += region[x][y] * SOBEL_Y[x][y]

            magnitude = int(math.sqrt(gradient_x ** 2 + gradient_y**2))
            magnitude = max(0, min(magnitude, 255))
            new_row.append(magnitude)
        new_image.append(new_row)

    return new_image

def apply_median_filter(image, kernel) -> list:
    """
    Median filter works by applying the median of the values of the neighbours to a pixel
    """
    height = len(image)
    width = len(image[0]) if height > 0 else 0
    kernel_size = len(kernel)
    pad = kernel_size // 2
    new_image = []

    # Pad the image with zeros
    padded_image = [[0] * (width + 2 * pad) for _ in range(height + 2 * pad)]
    for i in range(height):
        for j in range(width):
            padded_image[i + pad][j + pad] = image[i][j]

    for i in range(height):
        new_row = []
        for j in range(width):
            window = []
            for dx in range(-pad, pad + 1):
                for dy in range(-pad, pad + 1):
                    x = i + pad + dx
                    y = j + pad + dy
                    window.append(padded_image[x][y])
            
            # Find median value
            median = sorted(window)[len(window) // 2]
            new_row.append(median)
        new_image.append(new_row)
    
    return new_image