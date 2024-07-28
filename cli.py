import argparse
from module.image_processing import convert_image

def main():
    parser = argparse.ArgumentParser(description="Convert and resize images.")
    parser.add_argument("input_file", help="Path to the input image file")
    parser.add_argument("output_format", choices=["jpeg", "webp", "png", "gif", "tiff", "bmp"], help="Output image format")
    parser.add_argument("--max-width", "-mw", type=int, help="Maximum width for resizing", default=None)
    parser.add_argument("--max-height", "-mh", type=int, help="Maximum height for resizing", default=None)
    
    args = parser.parse_args()
    
    convert_image(args.input_file, args.output_format, args.max_width, args.max_height)

if __name__ == "__main__":
    main()