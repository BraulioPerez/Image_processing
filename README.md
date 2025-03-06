# Image Processing Application

A high-performance image processing application that implements various image filters (Gaussian blur, Sobel edge detection, and Median filter) in multiple implementations: Python, NumPy, and Cython. This project demonstrates the performance differences between implementations in different programming paradigms.

## Features
- Process images with multiple filter types:
  - Gaussian blur filter (for smoothing)
  - Sobel edge detection (for finding edges)
  - Median filter (for noise reduction)
- Compare performance across different implementations:
  - Pure Python
  - NumPy-accelerated Python
  - Cython-accelerated implementation
- Detailed performance measurements for benchmarking

## Team Members
- Braulio Pérez
- Oscar Martinez
- Moises Carrillo
- David Hernandez

## Project Structure

```
image_processing/
├── build/                        # Compiled files (generated)
├── cython/                       # Output directory for Cython processed images
├── numpy/                        # Output directory for NumPy processed images
├── python/                       # Output directory for Python processed images
├── image.jpeg                    # Sample input image
├── process_image_cython.pyx      # Cython implementation source
├── process_image_cython.c        # Generated C code (after Cython compilation)
├── process_image_numpy.py        # NumPy implementation
├── process_image_python.py       # Pure Python implementation
├── setup.py                      # Cython build configuration
├── test.py                       # Main test script
├── unit_test_cython.py           # Tests for Cython implementation
├── unit_test_numpy.py            # Tests for NumPy implementation
├── unit_test_python.py           # Tests for Python implementation
├── README.md                    
└── requirements.txt              # Project dependencies
```

## Installation

1. Clone the repository
2. Install dependencies:

```bash
# Windows
pip install -r requirements.txt

# Unix/macOS
pip3 install -r requirements.txt
```

3. Build the Cython extension:

```bash
# Windows
python setup.py build_ext --inplace

# Unix/macOS
python3 setup.py build_ext --inplace
```

## Usage Instructions

### Running Tests

To test a specific implementation:

```bash
# Windows
python unit_test_python.py  # Pure Python
python unit_test_numpy.py   # NumPy
python unit_test_cython.py  # Cython

# Unix/macOS
python3 unit_test_python.py  # Pure Python
python3 unit_test_numpy.py   # NumPy
python3 unit_test_cython.py  # Cython
```

Each test will generate output images in the corresponding implementation folder:
- `**/output_sobel_*.jpg`: Image with Sobel edge detection
- `**/output_gaussian_*.jpg`: Image with Gaussian blur
- `**/output_noise_reduction_*.jpg`: Image with median filter for noise reduction

The tests will also display processing times for each operation in the console.

## Implementation Details

The project implements three main image processing filters:

1. **Gaussian Blur**: Smooths the image using a Gaussian kernel
   - Configurable kernel size and sigma value
   - Includes padding for edge handling

2. **Sobel Edge Detection**: Detects edges using the Sobel operator
   - Implements both X and Y direction gradients
   - Combines gradients using magnitude calculation

3. **Median Filter**: Reduces noise by replacing each pixel with the median of neighboring pixels
   - Uses a sliding window approach
   - Configurable window size

## Performance Considerations

- The **Pure Python** implementation uses list comprehension and basic loops
- The **NumPy** implementation leverages vectorized operations for better performance
- The **Cython** implementation compiles to C for maximum performance
- Test results include timing measurements for each filter operation and implementation

## Troubleshooting

If you encounter an import error with the Cython module:

1. Make sure you've properly built the Cython extension:
   ```bash
   # Windows
   python setup.py build_ext --inplace
   
   # Unix/macOS
   python3 setup.py build_ext --inplace
   ```

2. Check that you're importing the module correctly:
   ```python
   # Correct import
   from process_image_cython import (
       read_image,
       save_image,
       create_gaussian_kernel,
       apply_filter,
       apply_sobel,
       apply_median_filter
   )
   ```

## Requirements

- Python 3.6+
- Required libraries listed in requirements.txt
- A compatible image file for processing (JPEG/JPG/PNG)# ssh
