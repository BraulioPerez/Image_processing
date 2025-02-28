from process_image_python import SOBEL_X, apply_sobel, read_image, save_image
import sys


def main():
    if len(sys.argv) != 3:
        print("Usage: python process_image_python.py <input_image> <output_image>")
        sys.exit(1)
    
    input_path = sys.argv[1]
    output_path = sys.argv[2]

    # Read image
    image = read_image(input_path)
    
    # Apply Sobel edge detection
    edge_image = apply_sobel(image, SOBEL_X)
    
    # Save the result
    save_image(edge_image, output_path)

if __name__ == "__main__":
    main()