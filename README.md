# Image Processing Application

A high-performance image processing application that implements Gaussian blur and Sobel edge detection filters in both Python and C++. This project demonstrates the performance differences between implementations in different programming languages.

## Features
- Upload images in JPG/JPEG/PNG formats
- Apply multiple filters in sequence:
  - Gaussian blur filter
  - Sobel edge detection
  - Combined filters (Gaussian + Sobel)
- Process images using either Python or C++ implementations
- Performance measurement and comparison

## Team Members
- Braulio Pérez
- Oscar Martinez
- Moises Carrillo
- David Hernandez

## Installation
1. Clone the repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage Instructions
### Python Implementation
To process an image using the Python implementation:

```bash
python process_image_python.py input_image.jpg output_image.jpg
```

### Running Tests
To run performance tests and generate sample outputs:

```bash
python unit_test.py
```

This will generate three output images:

- output_sobel.jpg: Image with Sobel edge detection
- output_gaussian.jpg: Image with Gaussian blur
- output_combined.jpg: Image with both filters applied

The test will also display processing times for each operation in the console.

## Project Structure

```bash
image_processing/
├── process_image_python.py  # Python implementation
├── unit_test.py            # Performance testing
├── README.md              
└── requirements.txt        
```

## mplementation Details
The project implements two main image processing filters:

1. Gaussian Blur: Smooths the image using a Gaussian kernel
  - Configurable kernel size and sigma value
  - Includes padding for edge handling
2. Sobel Edge Detection: Detects edges using the Sobel operator
  - Implements both X and Y direction gradients
  - Combines gradients using magnitude calculation

## Performance Considerations
- The Python implementation uses list comprehension and optimized matrix operations
- Test results include timing measurements for each filter operation
- Combined filter application (Gaussian + Sobel) demonstrates filter chaining

## Requirements
- Python 3.6+
- PIL (Python Imaging Library)
- A compatible image file for processing
